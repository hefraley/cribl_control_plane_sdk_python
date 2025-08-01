# UpdateCriblLakeDatasetByLakeIDAndIDRequest


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `lake_id`                                                | *str*                                                    | :heavy_check_mark:                                       | lake id that contains the Datasets                       |
| `id_param`                                               | *str*                                                    | :heavy_check_mark:                                       | dataset id to update                                     |
| `cribl_lake_dataset`                                     | [models.CriblLakeDataset](../models/cribllakedataset.md) | :heavy_check_mark:                                       | CriblLakeDataset object                                  |