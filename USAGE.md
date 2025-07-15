<!-- Start SDK Example Usage [usage] -->
```python
# Synchronous Example
from cribl_control_plane import CriblControlPlane


with CriblControlPlane(
    server_url="https://api.example.com",
) as ccp_client:

    res = ccp_client.auth.login(username="Nikko.Connelly", password="Ljp4BunfMR9hNyM")

    # Handle response
    print(res)
```

</br>

The same SDK client can also be used to make asychronous requests by importing asyncio.
```python
# Asynchronous Example
import asyncio
from cribl_control_plane import CriblControlPlane

async def main():

    async with CriblControlPlane(
        server_url="https://api.example.com",
    ) as ccp_client:

        res = await ccp_client.auth.login_async(username="Nikko.Connelly", password="Ljp4BunfMR9hNyM")

        # Handle response
        print(res)

asyncio.run(main())
```
<!-- End SDK Example Usage [usage] -->