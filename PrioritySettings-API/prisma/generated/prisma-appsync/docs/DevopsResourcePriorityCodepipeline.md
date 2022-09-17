# DevopsResourcePriorityCodepipeline

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePriorityCodepipeline` type.

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

-   `getDevopsResourcePriorityCodepipeline`: Read a single DevopsResourcePriorityCodepipeline.
-   `listDevopsResourcePriorityCodepipelines`: Read multiple DevopsResourcePriorityCodepipelines.
-   `countDevopsResourcePriorityCodepipelines`: Count all DevopsResourcePriorityCodepipelines.

### Querying a single DevopsResourcePriorityCodepipeline

Single DevopsResourcePriorityCodepipeline queries take one input:

-   `where`: `DevopsResourcePriorityCodepipelineWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePriorityCodepipeline(
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

### Querying multiple DevopsResourcePriorityCodepipelines

Multiple DevopsResourcePriorityCodepipelines queries can take four inputs:

-   `where`: `DevopsResourcePriorityCodepipelineWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityCodepipelineOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePriorityCodepipelines {
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
    listDevopsResourcePriorityCodepipelines(
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
    listDevopsResourcePriorityCodepipelines(
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
    listDevopsResourcePriorityCodepipelines(
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
    listDevopsResourcePriorityCodepipelines(
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

### Counting DevopsResourcePriorityCodepipelines

Counting DevopsResourcePriorityCodepipelines queries can take four inputs:

-   `where`: `DevopsResourcePriorityCodepipelineWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityCodepipelineOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePriorityCodepipelines
}
```

> `countDevopsResourcePriorityCodepipelines` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePriorityCodepipeline`: Create a single DevopsResourcePriorityCodepipeline.
-   `updateDevopsResourcePriorityCodepipeline`: Update a single DevopsResourcePriorityCodepipeline.
-   `upsertDevopsResourcePriorityCodepipeline`: Update existing OR create single DevopsResourcePriorityCodepipeline.
-   `deleteDevopsResourcePriorityCodepipeline`: Delete a single DevopsResourcePriorityCodepipeline.
-   `createManyDevopsResourcePriorityCodepipelines`: Create multiple DevopsResourcePriorityCodepipelines.
-   `updateManyDevopsResourcePriorityCodepipelines`: Update multiple DevopsResourcePriorityCodepipelines.
-   `deleteManyDevopsResourcePriorityCodepipelines`: Delete multiple DevopsResourcePriorityCodepipelines.

### Creating a single DevopsResourcePriorityCodepipeline

Single DevopsResourcePriorityCodepipeline create mutations take one input:

-   `data`: `DevopsResourcePriorityCodepipelineCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePriorityCodepipeline(
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

### Updating a single DevopsResourcePriorityCodepipeline

Single DevopsResourcePriorityCodepipeline update mutations take two inputs:

-   `where`: `DevopsResourcePriorityCodepipelineWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePriorityCodepipelineUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePriorityCodepipeline(
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

### Deleting a single DevopsResourcePriorityCodepipeline

Single DevopsResourcePriorityCodepipeline delete mutations take one input:

-   `where`: `DevopsResourcePriorityCodepipelineWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePriorityCodepipeline(
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

### Creating multiple DevopsResourcePriorityCodepipelines

Multiple DevopsResourcePriorityCodepipelines create mutations take one input:

-   `data`: `[DevopsResourcePriorityCodepipelineCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePriorityCodepipelines(
        data: [{ count: 2 }, { count: 2 }, { count: 2 }]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsResourcePriorityCodepipelines` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePriorityCodepipelines

Multiple DevopsResourcePriorityCodepipelines update mutations take two inputs:

-   `where`: `DevopsResourcePriorityCodepipelineWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePriorityCodepipelineUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePriorityCodepipelines(
        where: { count: 2 }
        data: { count: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePriorityCodepipelines` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePriorityCodepipelines

Multiple DevopsResourcePriorityCodepipelines delete mutations can take one input:

-   `where`: `DevopsResourcePriorityCodepipelineWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePriorityCodepipelines(
        where: { count: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePriorityCodepipelines` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePriorityCodepipeline creation

Triggered from `createDevopsResourcePriorityCodepipeline` mutation (excl. `createManyDevopsResourcePriorityCodepipelines` and `upsertDevopsResourcePriorityCodepipeline`).

```graphql
subscription {
    onCreatedDevopsResourcePriorityCodepipeline {
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

### Subscribing to a single DevopsResourcePriorityCodepipeline update

Triggered from `updateDevopsResourcePriorityCodepipeline` mutation (excl. `updateManyDevopsResourcePriorityCodepipelines` and `upsertDevopsResourcePriorityCodepipeline`).

```graphql
subscription {
    onUpdatedDevopsResourcePriorityCodepipeline {
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

### Subscribing to a single DevopsResourcePriorityCodepipeline upsert

Triggered from `upsertDevopsResourcePriorityCodepipeline` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePriorityCodepipeline {
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

### Subscribing to a single DevopsResourcePriorityCodepipeline deletion

Triggered from `deleteDevopsResourcePriorityCodepipeline` mutation (excl. `deleteManyDevopsResourcePriorityCodepipelines`).

```graphql
subscription {
    onDeletedDevopsResourcePriorityCodepipeline {
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

### Subscribing to a single DevopsResourcePriorityCodepipeline mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePriorityCodepipelines`).

```graphql
subscription {
    onMutatedDevopsResourcePriorityCodepipeline {
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

### Subscribing to many DevopsResourcePriorityCodepipeline creations

Triggered from `createManyDevopsResourcePriorityCodepipelines` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePriorityCodepipelines {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCodepipeline updates

Triggered from `updateManyDevopsResourcePriorityCodepipelines` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePriorityCodepipelines {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCodepipeline deletions

Triggered from `deleteManyDevopsResourcePriorityCodepipelines` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePriorityCodepipelines {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCodepipeline mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePriorityCodepipelines {
        count
    }
}
```
