# Lake
(*lake*)

## Overview

Actions related to Lake

### Available Operations

* [create_cribl_lake_dataset_by_lake_id](#create_cribl_lake_dataset_by_lake_id) - Create a Dataset in the specified Lake
* [get_cribl_lake_dataset_by_lake_id](#get_cribl_lake_dataset_by_lake_id) - Get the list of Dataset contained in the specified Lake
* [delete_cribl_lake_dataset_by_lake_id_and_id](#delete_cribl_lake_dataset_by_lake_id_and_id) - Delete a Dataset in the specified Lake
* [get_cribl_lake_dataset_by_lake_id_and_id](#get_cribl_lake_dataset_by_lake_id_and_id) - Get a Dataset in the specified Lake
* [update_cribl_lake_dataset_by_lake_id_and_id](#update_cribl_lake_dataset_by_lake_id_and_id) - Update a Dataset in the specified Lake

## create_cribl_lake_dataset_by_lake_id

Create a Dataset in the specified Lake

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake.create_cribl_lake_dataset_by_lake_id(lake_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `lake_id`                                                                           | *str*                                                                               | :heavy_check_mark:                                                                  | lake id that contains the Datasets                                                  |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `accelerated_fields`                                                                | List[*str*]                                                                         | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `bucket_name`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `cache_connection`                                                                  | [Optional[models.CacheConnection]](../../models/cacheconnection.md)                 | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `deletion_started_at`                                                               | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `format_`                                                                           | [Optional[models.CriblLakeDatasetFormat]](../../models/cribllakedatasetformat.md)   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `http_da_used`                                                                      | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retention_period_in_days`                                                          | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `search_config`                                                                     | [Optional[models.LakeDatasetSearchConfig]](../../models/lakedatasetsearchconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `storage_location_id`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `view_name`                                                                         | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.CreateCriblLakeDatasetByLakeIDResponse](../../models/createcribllakedatasetbylakeidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get_cribl_lake_dataset_by_lake_id

Get the list of Dataset contained in the specified Lake

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake.get_cribl_lake_dataset_by_lake_id(lake_id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `lake_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | lake id that contains the Datasets                                  |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCriblLakeDatasetByLakeIDResponse](../../models/getcribllakedatasetbylakeidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## delete_cribl_lake_dataset_by_lake_id_and_id

Delete a Dataset in the specified Lake

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake.delete_cribl_lake_dataset_by_lake_id_and_id(lake_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `lake_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | lake id that contains the Datasets                                  |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | dataset id to delete                                                |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.DeleteCriblLakeDatasetByLakeIDAndIDResponse](../../models/deletecribllakedatasetbylakeidandidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## get_cribl_lake_dataset_by_lake_id_and_id

Get a Dataset in the specified Lake

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake.get_cribl_lake_dataset_by_lake_id_and_id(lake_id="<id>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `lake_id`                                                           | *str*                                                               | :heavy_check_mark:                                                  | lake id that contains the Datasets                                  |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | dataset id to get                                                   |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.GetCriblLakeDatasetByLakeIDAndIDResponse](../../models/getcribllakedatasetbylakeidandidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |

## update_cribl_lake_dataset_by_lake_id_and_id

Update a Dataset in the specified Lake

### Example Usage

```python
from cribl_control_plane import CriblControlPlane, models
import os


with CriblControlPlane(
    server_url="https://api.example.com",
    security=models.Security(
        bearer_auth=os.getenv("CRIBLCONTROLPLANE_BEARER_AUTH", ""),
    ),
) as ccp_client:

    res = ccp_client.lake.update_cribl_lake_dataset_by_lake_id_and_id(lake_id="<id>", id_param="<value>", id="<id>")

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                           | Type                                                                                | Required                                                                            | Description                                                                         |
| ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| `lake_id`                                                                           | *str*                                                                               | :heavy_check_mark:                                                                  | lake id that contains the Datasets                                                  |
| `id_param`                                                                          | *str*                                                                               | :heavy_check_mark:                                                                  | dataset id to update                                                                |
| `id`                                                                                | *str*                                                                               | :heavy_check_mark:                                                                  | N/A                                                                                 |
| `accelerated_fields`                                                                | List[*str*]                                                                         | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `bucket_name`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `cache_connection`                                                                  | [Optional[models.CacheConnection]](../../models/cacheconnection.md)                 | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `deletion_started_at`                                                               | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `description`                                                                       | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `format_`                                                                           | [Optional[models.CriblLakeDatasetFormat]](../../models/cribllakedatasetformat.md)   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `http_da_used`                                                                      | *Optional[bool]*                                                                    | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retention_period_in_days`                                                          | *Optional[float]*                                                                   | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `search_config`                                                                     | [Optional[models.LakeDatasetSearchConfig]](../../models/lakedatasetsearchconfig.md) | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `storage_location_id`                                                               | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `view_name`                                                                         | *Optional[str]*                                                                     | :heavy_minus_sign:                                                                  | N/A                                                                                 |
| `retries`                                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                    | :heavy_minus_sign:                                                                  | Configuration to override the default retry behavior of the client.                 |

### Response

**[models.UpdateCriblLakeDatasetByLakeIDAndIDResponse](../../models/updatecribllakedatasetbylakeidandidresponse.md)**

### Errors

| Error Type       | Status Code      | Content Type     |
| ---------------- | ---------------- | ---------------- |
| errors.Error     | 500              | application/json |
| errors.APIError  | 4XX, 5XX         | \*/\*            |