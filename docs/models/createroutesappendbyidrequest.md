# CreateRoutesAppendByIDRequest


## Fields

| Field                                                                             | Type                                                                              | Required                                                                          | Description                                                                       |
| --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `id`                                                                              | *str*                                                                             | :heavy_check_mark:                                                                | the route table to be appended to - currently default is the only supported value |
| `request_body`                                                                    | List[[models.RouteConf](../models/routeconf.md)]                                  | :heavy_check_mark:                                                                | RouteDefinitions object                                                           |