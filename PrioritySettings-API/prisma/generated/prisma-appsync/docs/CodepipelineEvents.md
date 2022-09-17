# CodepipelineEvents

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `CodepipelineEvents` type.

| Field                 | Scalar Type | Unique  | Required (create) |
| --------------------- | ----------- | ------- | ----------------- |
| region                | String      | _false_ | _false_           |
| time                  | String      | _false_ | _false_           |
| source                | String      | _false_ | _false_           |
| resource              | String      | _false_ | _false_           |
| action                | String      | _false_ | _false_           |
| state                 | String      | _false_ | _false_           |
| costly_resource_avg   | Int         | _false_ | _false_           |
| resource_priority_avg | Int         | _false_ | _false_           |
| detail_type           | String      | _false_ | _false_           |
| id                    | Int         | true    | true              |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getCodepipelineEvents`: Read a single CodepipelineEvents.
-   `listCodepipelineEvents`: Read multiple CodepipelineEvents.
-   `countCodepipelineEvents`: Count all CodepipelineEvents.

### Querying a single CodepipelineEvents

Single CodepipelineEvents queries take one input:

-   `where`: `CodepipelineEventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getCodepipelineEvents(where: { id: 2 }) {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Querying multiple CodepipelineEvents

Multiple CodepipelineEvents queries can take four inputs:

-   `where`: `CodepipelineEventsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[CodepipelineEventsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listCodepipelineEvents {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listCodepipelineEvents(skip: 0, take: 25) {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listCodepipelineEvents(
        where: { region: { equals: "Foo" } }
    ) {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listCodepipelineEvents(
        where: { region: { not: { equals: "Foo" } } }
    ) {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listCodepipelineEvents(
        orderBy: [{ region: DESC }, { time: ASC }]
    ) {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Counting CodepipelineEvents

Counting CodepipelineEvents queries can take four inputs:

-   `where`: `CodepipelineEventsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[CodepipelineEventsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countCodepipelineEvents
}
```

> `countCodepipelineEvents` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createCodepipelineEvents`: Create a single CodepipelineEvents.
-   `updateCodepipelineEvents`: Update a single CodepipelineEvents.
-   `upsertCodepipelineEvents`: Update existing OR create single CodepipelineEvents.
-   `deleteCodepipelineEvents`: Delete a single CodepipelineEvents.
-   `createManyCodepipelineEvents`: Create multiple CodepipelineEvents.
-   `updateManyCodepipelineEvents`: Update multiple CodepipelineEvents.
-   `deleteManyCodepipelineEvents`: Delete multiple CodepipelineEvents.

### Creating a single CodepipelineEvents

Single CodepipelineEvents create mutations take one input:

-   `data`: `CodepipelineEventsCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createCodepipelineEvents(
        data: {
            region: "Foo"
            time: "Foo"
            source: "Foo"
            resource: "Foo"
            action: "Foo"
            state: "Foo"
            costly_resource_avg: 2
            resource_priority_avg: 2
            detail_type: "Foo"
        }
    ) {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Updating a single CodepipelineEvents

Single CodepipelineEvents update mutations take two inputs:

-   `where`: `CodepipelineEventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `CodepipelineEventsUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateCodepipelineEvents(
        where: { id: 2 }
        data: {
            region: "Foo"
            time: "Foo"
            source: "Foo"
            resource: "Foo"
            action: "Foo"
            state: "Foo"
            costly_resource_avg: 2
            resource_priority_avg: 2
            detail_type: "Foo"
        }
    ) {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Deleting a single CodepipelineEvents

Single CodepipelineEvents delete mutations take one input:

-   `where`: `CodepipelineEventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteCodepipelineEvents(where: { id: 2 }) {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Creating multiple CodepipelineEvents

Multiple CodepipelineEvents create mutations take one input:

-   `data`: `[CodepipelineEventsCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyCodepipelineEvents(
        data: [
            { region: "Foo" }
            { region: "Foo" }
            { region: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyCodepipelineEvents` returns an integer that represents the number of records that were created.

### Updating multiple CodepipelineEvents

Multiple CodepipelineEvents update mutations take two inputs:

-   `where`: `CodepipelineEventsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `CodepipelineEventsUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyCodepipelineEvents(
        where: { region: "Foo" }
        data: { region: "Foo" }
    ) {
        count
    }
}
```

> `updateManyCodepipelineEvents` returns an integer that represents the number of records that were updated.

### Deleting multiple CodepipelineEvents

Multiple CodepipelineEvents delete mutations can take one input:

-   `where`: `CodepipelineEventsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyCodepipelineEvents(where: { region: "Foo" }) {
        count
    }
}
```

> `deleteManyCodepipelineEvents` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single CodepipelineEvents creation

Triggered from `createCodepipelineEvents` mutation (excl. `createManyCodepipelineEvents` and `upsertCodepipelineEvents`).

```graphql
subscription {
    onCreatedCodepipelineEvents {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Subscribing to a single CodepipelineEvents update

Triggered from `updateCodepipelineEvents` mutation (excl. `updateManyCodepipelineEvents` and `upsertCodepipelineEvents`).

```graphql
subscription {
    onUpdatedCodepipelineEvents {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Subscribing to a single CodepipelineEvents upsert

Triggered from `upsertCodepipelineEvents` mutation.

```graphql
subscription {
    onUpsertedCodepipelineEvents {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Subscribing to a single CodepipelineEvents deletion

Triggered from `deleteCodepipelineEvents` mutation (excl. `deleteManyCodepipelineEvents`).

```graphql
subscription {
    onDeletedCodepipelineEvents {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Subscribing to a single CodepipelineEvents mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyCodepipelineEvents`).

```graphql
subscription {
    onMutatedCodepipelineEvents {
        region
        time
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
    }
}
```

### Subscribing to many CodepipelineEvents creations

Triggered from `createManyCodepipelineEvents` mutation.

```graphql
subscription {
    onCreatedManyCodepipelineEvents {
        count
    }
}
```

### Subscribing to many CodepipelineEvents updates

Triggered from `updateManyCodepipelineEvents` mutation.

```graphql
subscription {
    onUpdatedManyCodepipelineEvents {
        count
    }
}
```

### Subscribing to many CodepipelineEvents deletions

Triggered from `deleteManyCodepipelineEvents` mutation.

```graphql
subscription {
    onDeletedManyCodepipelineEvents {
        count
    }
}
```

### Subscribing to many CodepipelineEvents mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyCodepipelineEvents {
        count
    }
}
```
