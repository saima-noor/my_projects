# DevopsCostlyResourceEcsTask

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceEcsTask` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| cluster_name             | String      | _false_ | _false_           |
| service_name             | String      | _false_ | _false_           |
| task_name                | String      | _false_ | _false_           |
| container_count          | Int         | _false_ | _false_           |
| start_time               | AWSDateTime | _false_ | _false_           |
| priority                 | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceEcsTask`: Read a single DevopsCostlyResourceEcsTask.
-   `listDevopsCostlyResourceEcsTasks`: Read multiple DevopsCostlyResourceEcsTasks.
-   `countDevopsCostlyResourceEcsTasks`: Count all DevopsCostlyResourceEcsTasks.

### Querying a single DevopsCostlyResourceEcsTask

Single DevopsCostlyResourceEcsTask queries take one input:

-   `where`: `DevopsCostlyResourceEcsTaskWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceEcsTask(where: { id: 2 }) {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsCostlyResourceEcsTasks

Multiple DevopsCostlyResourceEcsTasks queries can take four inputs:

-   `where`: `DevopsCostlyResourceEcsTaskWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceEcsTaskOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceEcsTasks {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
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
    listDevopsCostlyResourceEcsTasks(skip: 0, take: 25) {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
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
    listDevopsCostlyResourceEcsTasks(
        where: { cluster_name: { equals: "Foo" } }
    ) {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
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
    listDevopsCostlyResourceEcsTasks(
        where: { cluster_name: { not: { equals: "Foo" } } }
    ) {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
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
    listDevopsCostlyResourceEcsTasks(
        orderBy: [
            { cluster_name: DESC }
            { service_name: ASC }
        ]
    ) {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsCostlyResourceEcsTasks

Counting DevopsCostlyResourceEcsTasks queries can take four inputs:

-   `where`: `DevopsCostlyResourceEcsTaskWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceEcsTaskOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceEcsTasks
}
```

> `countDevopsCostlyResourceEcsTasks` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceEcsTask`: Create a single DevopsCostlyResourceEcsTask.
-   `updateDevopsCostlyResourceEcsTask`: Update a single DevopsCostlyResourceEcsTask.
-   `upsertDevopsCostlyResourceEcsTask`: Update existing OR create single DevopsCostlyResourceEcsTask.
-   `deleteDevopsCostlyResourceEcsTask`: Delete a single DevopsCostlyResourceEcsTask.
-   `createManyDevopsCostlyResourceEcsTasks`: Create multiple DevopsCostlyResourceEcsTasks.
-   `updateManyDevopsCostlyResourceEcsTasks`: Update multiple DevopsCostlyResourceEcsTasks.
-   `deleteManyDevopsCostlyResourceEcsTasks`: Delete multiple DevopsCostlyResourceEcsTasks.

### Creating a single DevopsCostlyResourceEcsTask

Single DevopsCostlyResourceEcsTask create mutations take one input:

-   `data`: `DevopsCostlyResourceEcsTaskCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceEcsTask(
        data: {
            cluster_name: "Foo"
            service_name: "Foo"
            task_name: "Foo"
            container_count: 2
            start_time: "dd/mm/YYYY"
            priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsCostlyResourceEcsTask

Single DevopsCostlyResourceEcsTask update mutations take two inputs:

-   `where`: `DevopsCostlyResourceEcsTaskWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceEcsTaskUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceEcsTask(
        where: { id: 2 }
        data: {
            cluster_name: "Foo"
            service_name: "Foo"
            task_name: "Foo"
            container_count: 2
            start_time: "dd/mm/YYYY"
            priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsCostlyResourceEcsTask

Single DevopsCostlyResourceEcsTask delete mutations take one input:

-   `where`: `DevopsCostlyResourceEcsTaskWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceEcsTask(where: { id: 2 }) {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsCostlyResourceEcsTasks

Multiple DevopsCostlyResourceEcsTasks create mutations take one input:

-   `data`: `[DevopsCostlyResourceEcsTaskCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceEcsTasks(
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

> `createManyDevopsCostlyResourceEcsTasks` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceEcsTasks

Multiple DevopsCostlyResourceEcsTasks update mutations take two inputs:

-   `where`: `DevopsCostlyResourceEcsTaskWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceEcsTaskUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceEcsTasks(
        where: { cluster_name: "Foo" }
        data: { cluster_name: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceEcsTasks` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceEcsTasks

Multiple DevopsCostlyResourceEcsTasks delete mutations can take one input:

-   `where`: `DevopsCostlyResourceEcsTaskWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceEcsTasks(
        where: { cluster_name: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceEcsTasks` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceEcsTask creation

Triggered from `createDevopsCostlyResourceEcsTask` mutation (excl. `createManyDevopsCostlyResourceEcsTasks` and `upsertDevopsCostlyResourceEcsTask`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceEcsTask {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceEcsTask update

Triggered from `updateDevopsCostlyResourceEcsTask` mutation (excl. `updateManyDevopsCostlyResourceEcsTasks` and `upsertDevopsCostlyResourceEcsTask`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceEcsTask {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceEcsTask upsert

Triggered from `upsertDevopsCostlyResourceEcsTask` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceEcsTask {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceEcsTask deletion

Triggered from `deleteDevopsCostlyResourceEcsTask` mutation (excl. `deleteManyDevopsCostlyResourceEcsTasks`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceEcsTask {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceEcsTask mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceEcsTasks`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceEcsTask {
        id
        cluster_name
        service_name
        task_name
        container_count
        start_time
        priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsCostlyResourceEcsTask creations

Triggered from `createManyDevopsCostlyResourceEcsTasks` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceEcsTasks {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceEcsTask updates

Triggered from `updateManyDevopsCostlyResourceEcsTasks` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceEcsTasks {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceEcsTask deletions

Triggered from `deleteManyDevopsCostlyResourceEcsTasks` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceEcsTasks {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceEcsTask mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceEcsTasks {
        count
    }
}
```
