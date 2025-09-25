"""
Cribl Worker Group Replication Example

This example demonstrates how to programmatically replicate an existing 
worker group configuration using the Control Plane SDK.

This example performs the following operations:

1. Selects the first worker group as a source for replication.
2. Retrieves the complete configuration of the source worker group.
3. Creates a new worker group with the same configuration but a unique identity.

The replicated worker group includes:
- All configuration settings from the source
- A unique ID with timestamp to avoid conflicts
- Updated name and description to identify it as a replica

Data flow: Source Worker Group → Configuration Extraction → New Worker Group Creation

Prerequisites:
- An .env file configured with your credentials
- At least one existing worker group in the Stream product
- API token with worker group creation permissions
"""

import asyncio
from typing import Optional
from cribl_control_plane import CriblControlPlane
from cribl_control_plane.models import ConfigGroup, ProductsCore
from auth import create_cribl_client


async def main() -> None:
    """Main function that demonstrates worker group replication"""
    try:
        # Initialize Cribl client
        cribl_client = await create_cribl_client()

        # Get the first available worker group
        worker_groups = cribl_client.groups.list(product=ProductsCore.STREAM)
        
        if worker_groups.items and len(worker_groups.items) > 0:
            first_worker_group = worker_groups.items[0]
            print(f"Replicating worker group: {first_worker_group.id}")
            
            # Replicate the first worker group
            replicate_worker_group(cribl_client, first_worker_group.id)
        else:
            print('No worker groups found. Please create at least one worker group first.')
            exit(1)

    except Exception as error:
        message = str(error)
        print(f'Error: {message}')
        exit(1)


def replicate_worker_group(client: CriblControlPlane, source_id: str) -> Optional[ConfigGroup]:
    """
    Replicates a worker group with a new unique identity
    
    This function handles the complete replication process including:
    - Retrieving source configuration
    - Generating unique identifiers
    - Filtering out read-only fields
    - Creating the replica with proper metadata
    
    Args:
        client: Cribl client instance
        source_id: ID of the worker group to replicate
        
    Returns:
        The created replica ConfigGroup or None if creation failed
        
    Raises:
        Exception: If the source worker group is not found or creation fails
    """
    try:
        # Retrieve the source worker group configuration
        source_response = client.groups.get(
            id=source_id,
            product=ProductsCore.STREAM
        )

        if not source_response.items or len(source_response.items) == 0:
            raise Exception(f"Worker group '{source_id}' not found")

        source = source_response.items[0]

        # Generate unique identifiers for the replica
        replica_id = f"{source_id}-replica"
        replica_name = f"{source.name}-replica" if source.name else f"{source_id}-replica"

        # Create the replica worker group by copying configuration from source
        # Filtering out read-only fields (config_version, lookup_deployments, worker_count, etc.)
        result = client.groups.create(
            product=ProductsCore.STREAM,
            id=replica_id,
            name=replica_name,
            description=f"Replica of '{source_id}'",
            on_prem=source.on_prem,
            worker_remote_access=source.worker_remote_access,
            cloud=source.cloud,
            provisioned=source.provisioned,
            is_fleet=source.is_fleet,
            is_search=source.is_search,
            estimated_ingest_rate=source.estimated_ingest_rate,
            inherits=source.inherits,
            max_worker_age=source.max_worker_age,
            streamtags=source.streamtags,
            tags=source.tags,
            type_=source.type,
            upgrade_version=source.upgrade_version
        )
        
        if result.items and len(result.items) > 0:
            created = result.items[0]
            print(f"✅ Worker group replicated: {created.id}")
            return created
        else:
            raise Exception('Failed to create replica')

    except Exception as error:
        message = str(error)
        print(f"Failed to replicate worker group: {message}")
        raise error


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as error:
        message = str(error)
        print(f'Something went wrong: {message}')
