# DevopsCostlyResourceEcsService

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceEcsService` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| cluster_name             | String      | _false_ | _false_           |
| service_name             | String      | _false_ | _false_           |
| total_time_min           | Float       | _false_ | _false_           |
| priority                 | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceEcsService`: Read a single DevopsCostlyResourceEcsService.
-   `listDevopsCostlyResourceEcsServices`: Read multiple DevopsCostlyResourceEcsServices.
-   `countDevopsCostlyResourceEcsServices`: Count all DevopsCostlyResourceEcsServices.

### Querying a single DevopsCostlyResourceEcsService

Single DevopsCostlyResourceEcsService queries take one input:

-   `where`: `DevopsCostlyResourceEcsServiceWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceEcsService(where: { id: 2 }) {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsCostlyResourceEcsServices

Multiple DevopsCostlyResourceEcsServices queries can take four inputs:

-   `where`: `DevopsCostlyResourceEcsServiceWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceEcsServiceOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceEcsServices {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsCostlyResourceEcsServices(skip: 0, take: 25) {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsCostlyResourceEcsServices(
        where: { cluster_name: { equals: "Foo" } }
    ) {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsCostlyResourceEcsServices(
        where: { cluster_name: { not: { equals: "Foo" } } }
    ) {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsCostlyResourceEcsServices(
        orderBy: [
            { cluster_name: DESC }
            { service_name: ASC }
        ]
    ) {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsCostlyResourceEcsServices

Counting DevopsCostlyResourceEcsServices queries can take four inputs:

-   `where`: `DevopsCostlyResourceEcsServiceWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceEcsServiceOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceEcsServices
}
```

> `countDevopsCostlyResourceEcsServices` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceEcsService`: Create a single DevopsCostlyResourceEcsService.
-   `updateDevopsCostlyResourceEcsService`: Update a single DevopsCostlyResourceEcsService.
-   `upsertDevopsCostlyResourceEcsService`: Update existing OR create single DevopsCostlyResourceEcsService.
-   `deleteDevopsCostlyResourceEcsService`: Delete a single DevopsCostlyResourceEcsService.
-   `createManyDevopsCostlyResourceEcsServices`: Create multiple DevopsCostlyResourceEcsServices.
-   `updateManyDevopsCostlyResourceEcsServices`: Update multiple DevopsCostlyResourceEcsServices.
-   `deleteManyDevopsCostlyResourceEcsServices`: Delete multiple DevopsCostlyResourceEcsServices.

### Creating a single DevopsCostlyResourceEcsService

Single DevopsCostlyResourceEcsService create mutations take one input:

-   `data`: `DevopsCostlyResourceEcsServiceCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceEcsService(
        data: {
            cluster_name: "Foo"
            service_name: "Foo"
            total_time_min: 2.5
            priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsCostlyResourceEcsService

Single DevopsCostlyResourceEcsService update mutations take two inputs:

-   `where`: `DevopsCostlyResourceEcsServiceWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceEcsServiceUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceEcsService(
        where: { id: 2 }
        data: {
            cluster_name: "Foo"
            service_name: "Foo"
            total_time_min: 2.5
            priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsCostlyResourceEcsService

Single DevopsCostlyResourceEcsService delete mutations take one input:

-   `where`: `DevopsCostlyResourceEcsServiceWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceEcsService(where: { id: 2 }) {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsCostlyResourceEcsServices

Multiple DevopsCostlyResourceEcsServices create mutations take one input:

-   `data`: `[DevopsCostlyResourceEcsServiceCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceEcsServices(
        data: [
            { cluster_name: "Foo" }
            { cluster_name: "Foo" }
            { cluster_name: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsCostlyResourceEcsServices` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceEcsServices

Multiple DevopsCostlyResourceEcsServices update mutations take two inputs:

-   `where`: `DevopsCostlyResourceEcsServiceWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceEcsServiceUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceEcsServices(
        where: { cluster_name: "Foo" }
        data: { cluster_name: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceEcsServices` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceEcsServices

Multiple DevopsCostlyResourceEcsServices delete mutations can take one input:

-   `where`: `DevopsCostlyResourceEcsServiceWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceEcsServices(
        where: { cluster_name: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceEcsServices` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceEcsService creation

Triggered from `createDevopsCostlyResourceEcsService` mutation (excl. `createManyDevopsCostlyResourceEcsServices` and `upsertDevopsCostlyResourceEcsService`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceEcsService {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceEcsService update

Triggered from `updateDevopsCostlyResourceEcsService` mutation (excl. `updateManyDevopsCostlyResourceEcsServices` and `upsertDevopsCostlyResourceEcsService`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceEcsService {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceEcsService upsert

Triggered from `upsertDevopsCostlyResourceEcsService` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceEcsService {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceEcsService deletion

Triggered from `deleteDevopsCostlyResourceEcsService` mutation (excl. `deleteManyDevopsCostlyResourceEcsServices`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceEcsService {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceEcsService mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceEcsServices`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceEcsService {
        id
        cluster_name
        service_name
        total_time_min
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsCostlyResourceEcsService creations

Triggered from `createManyDevopsCostlyResourceEcsServices` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceEcsServices {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceEcsService updates

Triggered from `updateManyDevopsCostlyResourceEcsServices` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceEcsServices {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceEcsService deletions

Triggered from `deleteManyDevopsCostlyResourceEcsServices` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceEcsServices {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceEcsService mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceEcsServices {
        count
    }
}
```
