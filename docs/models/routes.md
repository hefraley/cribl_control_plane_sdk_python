# Routes


## Fields

| Field                                                | Type                                                 | Required                                             | Description                                          |
| ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- | ---------------------------------------------------- |
| `id`                                                 | *Optional[str]*                                      | :heavy_minus_sign:                                   | Routes ID                                            |
| `routes`                                             | List[[models.RoutesRoute](../models/routesroute.md)] | :heavy_check_mark:                                   | Pipeline routing rules                               |
| `groups`                                             | Dict[str, [models.Groups](../models/groups.md)]      | :heavy_minus_sign:                                   | N/A                                                  |
| `comments`                                           | List[[models.Comment](../models/comment.md)]         | :heavy_minus_sign:                                   | Comments                                             |