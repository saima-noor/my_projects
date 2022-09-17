# DevopsCostlyResourceCodepipeline

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceCodepipeline` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| pipeline_name            | String      | true    | _false_           |
| count                    | Int         | _false_ | _false_           |
| pipe_priority            | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceCodepipeline`: Read a single DevopsCostlyResourceCodepipeline.
-   `listDevopsCostlyResourceCodepipelines`: Read multiple DevopsCostlyResourceCodepipelines.
-   `countDevopsCostlyResourceCodepipelines`: Count all DevopsCostlyResourceCodepipelines.

### Querying a single DevopsCostlyResourceCodepipeline

Single DevopsCostlyResourceCodepipeline queries take one input:

-   `where`: `DevopsCostlyResourceCodepipelineWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceCodepipeline(where: { id: 2 }) {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsCostlyResourceCodepipelines

Multiple DevopsCostlyResourceCodepipelines queries can take four inputs:

-   `where`: `DevopsCostlyResourceCodepipelineWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceCodepipelineOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceCodepipelines {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsCostlyResourceCodepipelines(
        skip: 0
        take: 25
    ) {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsCostlyResourceCodepipelines(
        where: { count: { equals: 2 } }
    ) {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsCostlyResourceCodepipelines(
        where: { count: { not: { equals: 2 } } }
    ) {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsCostlyResourceCodepipelines(
        orderBy: [{ count: DESC }, { pipe_priority: ASC }]
    ) {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsCostlyResourceCodepipelines

Counting DevopsCostlyResourceCodepipelines queries can take four inputs:

-   `where`: `DevopsCostlyResourceCodepipelineWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceCodepipelineOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceCodepipelines
}
```

> `countDevopsCostlyResourceCodepipelines` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceCodepipeline`: Create a single DevopsCostlyResourceCodepipeline.
-   `updateDevopsCostlyResourceCodepipeline`: Update a single DevopsCostlyResourceCodepipeline.
-   `upsertDevopsCostlyResourceCodepipeline`: Update existing OR create single DevopsCostlyResourceCodepipeline.
-   `deleteDevopsCostlyResourceCodepipeline`: Delete a single DevopsCostlyResourceCodepipeline.
-   `createManyDevopsCostlyResourceCodepipelines`: Create multiple DevopsCostlyResourceCodepipelines.
-   `updateManyDevopsCostlyResourceCodepipelines`: Update multiple DevopsCostlyResourceCodepipelines.
-   `deleteManyDevopsCostlyResourceCodepipelines`: Delete multiple DevopsCostlyResourceCodepipelines.

### Creating a single DevopsCostlyResourceCodepipeline

Single DevopsCostlyResourceCodepipeline create mutations take one input:

-   `data`: `DevopsCostlyResourceCodepipelineCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceCodepipeline(
        data: {
            pipeline_name: "Foo"
            count: 2
            pipe_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsCostlyResourceCodepipeline

Single DevopsCostlyResourceCodepipeline update mutations take two inputs:

-   `where`: `DevopsCostlyResourceCodepipelineWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceCodepipelineUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceCodepipeline(
        where: { id: 2 }
        data: {
            pipeline_name: "Foo"
            count: 2
            pipe_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsCostlyResourceCodepipeline

Single DevopsCostlyResourceCodepipeline delete mutations take one input:

-   `where`: `DevopsCostlyResourceCodepipelineWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceCodepipeline(
        where: { id: 2 }
    ) {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsCostlyResourceCodepipelines

Multiple DevopsCostlyResourceCodepipelines create mutations take one input:

-   `data`: `[DevopsCostlyResourceCodepipelineCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceCodepipelines(
        data: [{ count: 2 }, { count: 2 }, { count: 2 }]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsCostlyResourceCodepipelines` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceCodepipelines

Multiple DevopsCostlyResourceCodepipelines update mutations take two inputs:

-   `where`: `DevopsCostlyResourceCodepipelineWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceCodepipelineUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceCodepipelines(
        where: { count: 2 }
        data: { count: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceCodepipelines` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceCodepipelines

Multiple DevopsCostlyResourceCodepipelines delete mutations can take one input:

-   `where`: `DevopsCostlyResourceCodepipelineWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceCodepipelines(
        where: { count: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceCodepipelines` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceCodepipeline creation

Triggered from `createDevopsCostlyResourceCodepipeline` mutation (excl. `createManyDevopsCostlyResourceCodepipelines` and `upsertDevopsCostlyResourceCodepipeline`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceCodepipeline {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodepipeline update

Triggered from `updateDevopsCostlyResourceCodepipeline` mutation (excl. `updateManyDevopsCostlyResourceCodepipelines` and `upsertDevopsCostlyResourceCodepipeline`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceCodepipeline {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodepipeline upsert

Triggered from `upsertDevopsCostlyResourceCodepipeline` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceCodepipeline {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodepipeline deletion

Triggered from `deleteDevopsCostlyResourceCodepipeline` mutation (excl. `deleteManyDevopsCostlyResourceCodepipelines`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceCodepipeline {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodepipeline mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceCodepipelines`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceCodepipeline {
        id
        pipeline_name
        count
        pipe_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsCostlyResourceCodepipeline creations

Triggered from `createManyDevopsCostlyResourceCodepipelines` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceCodepipelines {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodepipeline updates

Triggered from `updateManyDevopsCostlyResourceCodepipelines` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceCodepipelines {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodepipeline deletions

Triggered from `deleteManyDevopsCostlyResourceCodepipelines` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceCodepipelines {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodepipeline mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceCodepipelines {
        count
    }
}
```
