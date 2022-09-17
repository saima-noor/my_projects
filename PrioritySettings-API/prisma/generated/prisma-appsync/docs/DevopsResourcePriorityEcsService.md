# DevopsResourcePriorityEcsService

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePriorityEcsService` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| cluster_name             | String      | _false_ | _false_           |
| service_name             | String      | _false_ | _false_           |
| cpu                      | Float       | _false_ | _false_           |
| memory                   | Float       | _false_ | _false_           |
| priority                 | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsResourcePriorityEcsService`: Read a single DevopsResourcePriorityEcsService.
-   `listDevopsResourcePriorityEcsServices`: Read multiple DevopsResourcePriorityEcsServices.
-   `countDevopsResourcePriorityEcsServices`: Count all DevopsResourcePriorityEcsServices.

### Querying a single DevopsResourcePriorityEcsService

Single DevopsResourcePriorityEcsService queries take one input:

-   `where`: `DevopsResourcePriorityEcsServiceWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePriorityEcsService(where: { id: 2 }) {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsResourcePriorityEcsServices

Multiple DevopsResourcePriorityEcsServices queries can take four inputs:

-   `where`: `DevopsResourcePriorityEcsServiceWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityEcsServiceOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePriorityEcsServices {
        id
        cluster_name
        service_name
        cpu
        memory
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
    listDevopsResourcePriorityEcsServices(
        skip: 0
        take: 25
    ) {
        id
        cluster_name
        service_name
        cpu
        memory
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
    listDevopsResourcePriorityEcsServices(
        where: { cluster_name: { equals: "Foo" } }
    ) {
        id
        cluster_name
        service_name
        cpu
        memory
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
    listDevopsResourcePriorityEcsServices(
        where: { cluster_name: { not: { equals: "Foo" } } }
    ) {
        id
        cluster_name
        service_name
        cpu
        memory
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
    listDevopsResourcePriorityEcsServices(
        orderBy: [
            { cluster_name: DESC }
            { service_name: ASC }
        ]
    ) {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsResourcePriorityEcsServices

Counting DevopsResourcePriorityEcsServices queries can take four inputs:

-   `where`: `DevopsResourcePriorityEcsServiceWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityEcsServiceOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePriorityEcsServices
}
```

> `countDevopsResourcePriorityEcsServices` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePriorityEcsService`: Create a single DevopsResourcePriorityEcsService.
-   `updateDevopsResourcePriorityEcsService`: Update a single DevopsResourcePriorityEcsService.
-   `upsertDevopsResourcePriorityEcsService`: Update existing OR create single DevopsResourcePriorityEcsService.
-   `deleteDevopsResourcePriorityEcsService`: Delete a single DevopsResourcePriorityEcsService.
-   `createManyDevopsResourcePriorityEcsServices`: Create multiple DevopsResourcePriorityEcsServices.
-   `updateManyDevopsResourcePriorityEcsServices`: Update multiple DevopsResourcePriorityEcsServices.
-   `deleteManyDevopsResourcePriorityEcsServices`: Delete multiple DevopsResourcePriorityEcsServices.

### Creating a single DevopsResourcePriorityEcsService

Single DevopsResourcePriorityEcsService create mutations take one input:

-   `data`: `DevopsResourcePriorityEcsServiceCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePriorityEcsService(
        data: {
            cluster_name: "Foo"
            service_name: "Foo"
            cpu: 2.5
            memory: 2.5
            priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsResourcePriorityEcsService

Single DevopsResourcePriorityEcsService update mutations take two inputs:

-   `where`: `DevopsResourcePriorityEcsServiceWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePriorityEcsServiceUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePriorityEcsService(
        where: { id: 2 }
        data: {
            cluster_name: "Foo"
            service_name: "Foo"
            cpu: 2.5
            memory: 2.5
            priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsResourcePriorityEcsService

Single DevopsResourcePriorityEcsService delete mutations take one input:

-   `where`: `DevopsResourcePriorityEcsServiceWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePriorityEcsService(
        where: { id: 2 }
    ) {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsResourcePriorityEcsServices

Multiple DevopsResourcePriorityEcsServices create mutations take one input:

-   `data`: `[DevopsResourcePriorityEcsServiceCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePriorityEcsServices(
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

> `createManyDevopsResourcePriorityEcsServices` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePriorityEcsServices

Multiple DevopsResourcePriorityEcsServices update mutations take two inputs:

-   `where`: `DevopsResourcePriorityEcsServiceWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePriorityEcsServiceUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePriorityEcsServices(
        where: { cluster_name: "Foo" }
        data: { cluster_name: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePriorityEcsServices` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePriorityEcsServices

Multiple DevopsResourcePriorityEcsServices delete mutations can take one input:

-   `where`: `DevopsResourcePriorityEcsServiceWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePriorityEcsServices(
        where: { cluster_name: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePriorityEcsServices` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePriorityEcsService creation

Triggered from `createDevopsResourcePriorityEcsService` mutation (excl. `createManyDevopsResourcePriorityEcsServices` and `upsertDevopsResourcePriorityEcsService`).

```graphql
subscription {
    onCreatedDevopsResourcePriorityEcsService {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityEcsService update

Triggered from `updateDevopsResourcePriorityEcsService` mutation (excl. `updateManyDevopsResourcePriorityEcsServices` and `upsertDevopsResourcePriorityEcsService`).

```graphql
subscription {
    onUpdatedDevopsResourcePriorityEcsService {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityEcsService upsert

Triggered from `upsertDevopsResourcePriorityEcsService` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePriorityEcsService {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityEcsService deletion

Triggered from `deleteDevopsResourcePriorityEcsService` mutation (excl. `deleteManyDevopsResourcePriorityEcsServices`).

```graphql
subscription {
    onDeletedDevopsResourcePriorityEcsService {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityEcsService mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePriorityEcsServices`).

```graphql
subscription {
    onMutatedDevopsResourcePriorityEcsService {
        id
        cluster_name
        service_name
        cpu
        memory
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsResourcePriorityEcsService creations

Triggered from `createManyDevopsResourcePriorityEcsServices` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePriorityEcsServices {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityEcsService updates

Triggered from `updateManyDevopsResourcePriorityEcsServices` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePriorityEcsServices {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityEcsService deletions

Triggered from `deleteManyDevopsResourcePriorityEcsServices` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePriorityEcsServices {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityEcsService mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePriorityEcsServices {
        count
    }
}
```
