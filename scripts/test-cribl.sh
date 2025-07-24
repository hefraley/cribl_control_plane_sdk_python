#!/bin/bash

# =============================================================================
# Cribl Control Plane SDK - Real Server Testing Script
# =============================================================================
#
# This script automates testing the Cribl Control Plane SDK against a real
# Cribl Stream server running in Docker, as opposed to using mock servers.
#
# High-level workflow:
# 1. Find an available port for the Cribl server (starting from 9000)
# 2. Start a Cribl Stream Docker container if not already running
# 3. Wait for the server to become healthy by polling /api/v1/health
# 4. Authenticate with the server using admin credentials to get auth token
# 5. Set environment variables (TEST_SERVER_URL, TEST_BEARER_TOKEN)
# 6. Run Speakeasy SDK tests against the real server
# 7. Clean up the Docker container when done
#
# Usage:
#   ./scripts/cribl-test.sh      → Run tests against real Cribl server
#
# =============================================================================

# Function to find an available port
find_available_port() {
    local port=9000
    while lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1; do
        port=$((port + 1))
    done
    echo $port
}

# Find available port for Cribl server
CRIBL_PORT=$(find_available_port)
echo "Using port $CRIBL_PORT for Cribl server"

# Start Cribl server if not running
if ! docker ps | grep -q cribl-server-test-web-sdk; then
    echo "Starting Cribl server on port $CRIBL_PORT..."
    docker run -d --name cribl-server-test-web-sdk -p $CRIBL_PORT:9000 cribl/cribl:latest

    # Wait for startup
    echo "Waiting for Cribl server to be healthy..."
    timeout=120
    elapsed=0
    while [ $elapsed -lt $timeout ]; do
        if health_status=$(curl -s "http://localhost:${CRIBL_PORT}/api/v1/health" -H 'accept: application/json' 2>/dev/null) && \
           echo "$health_status" | jq -r '.status' | grep -q "healthy"; then
           echo "Cribl server is healthy!"
           break
        fi
        echo "Waiting... ($elapsed/${timeout}s)"
        sleep 1
        elapsed=$((elapsed + 1))
    done
    
    if [ $elapsed -ge $timeout ]; then
        echo "Timeout: Cribl server failed to become healthy within ${timeout} seconds"
        exit 1
    fi
fi

# Login to get auth token
response=$(curl -s -X 'POST' \
  "http://localhost:${CRIBL_PORT}/api/v1/auth/login" \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "username": "admin",
    "password": "admin"
   }')

# Extract the token using jq
authToken=$(echo "$response" | jq -r '.token')

if [ -z "$authToken" ] || [ "$authToken" = "null" ]; then
    echo "Error: Failed to retrieve auth token from login response"
    echo "Response: $response"
    exit 1
else
    echo "Auth token retrieved: $authToken"
fi

# Set correct API base URL with dynamic port
export TEST_SERVER_URL=http://localhost:$CRIBL_PORT/api/v1
# Set auth token to be used in tests
export TEST_BEARER_TOKEN=$authToken

# Run tests against real server using Speakeasy
echo "Running tests against real Cribl server at $TEST_SERVER_URL with auth token $TEST_BEARER_TOKEN"
speakeasy test --disable-mockserver

# Clean up when done
echo "Cleaning up..."
docker stop cribl-server-test-web-sdk && docker rm cribl-server-test-web-sdk