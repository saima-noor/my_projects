# ReclassificationEvents

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `ReclassificationEvents` type.

| Field                 | Scalar Type | Unique  | Required (create) |
| --------------------- | ----------- | ------- | ----------------- |
| region                | String      | _false_ | _false_           |
| source                | String      | _false_ | _false_           |
| resource              | String      | _false_ | _false_           |
| action                | String      | _false_ | _false_           |
| state                 | String      | _false_ | _false_           |
| costly_resource_avg   | Int         | _false_ | _false_           |
| resource_priority_avg | Int         | _false_ | _false_           |
| detail_type           | String      | _false_ | _false_           |
| id                    | Int         | true    | true              |
| time                  | AWSDateTime | _false_ | _false_           |
| region_priority       | Int         | _false_ | _false_           |
| service_priority      | Int         | _false_ | _false_           |
| resource_priority     | Int         | _false_ | _false_           |
| tag_priority          | Int         | _false_ | _false_           |
| resource_arn          | String      | _false_ | _false_           |
| quadrant              | String      | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getReclassificationEvents`: Read a single ReclassificationEvents.
-   `listReclassificationEvents`: Read multiple ReclassificationEvents.
-   `countReclassificationEvents`: Count all ReclassificationEvents.

### Querying a single ReclassificationEvents

Single ReclassificationEvents queries take one input:

-   `where`: `ReclassificationEventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getReclassificationEvents(where: { id: 2 }) {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Querying multiple ReclassificationEvents

Multiple ReclassificationEvents queries can take four inputs:

-   `where`: `ReclassificationEventsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[ReclassificationEventsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listReclassificationEvents {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listReclassificationEvents(skip: 0, take: 25) {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listReclassificationEvents(
        where: { region: { equals: "Foo" } }
    ) {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listReclassificationEvents(
        where: { region: { not: { equals: "Foo" } } }
    ) {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listReclassificationEvents(
        orderBy: [{ region: DESC }, { source: ASC }]
    ) {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Counting ReclassificationEvents

Counting ReclassificationEvents queries can take four inputs:

-   `where`: `ReclassificationEventsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[ReclassificationEventsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countReclassificationEvents
}
```

> `countReclassificationEvents` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createReclassificationEvents`: Create a single ReclassificationEvents.
-   `updateReclassificationEvents`: Update a single ReclassificationEvents.
-   `upsertReclassificationEvents`: Update existing OR create single ReclassificationEvents.
-   `deleteReclassificationEvents`: Delete a single ReclassificationEvents.
-   `createManyReclassificationEvents`: Create multiple ReclassificationEvents.
-   `updateManyReclassificationEvents`: Update multiple ReclassificationEvents.
-   `deleteManyReclassificationEvents`: Delete multiple ReclassificationEvents.

### Creating a single ReclassificationEvents

Single ReclassificationEvents create mutations take one input:

-   `data`: `ReclassificationEventsCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createReclassificationEvents(
        data: {
            region: "Foo"
            source: "Foo"
            resource: "Foo"
            action: "Foo"
            state: "Foo"
            costly_resource_avg: 2
            resource_priority_avg: 2
            detail_type: "Foo"
            time: "dd/mm/YYYY"
            region_priority: 2
            service_priority: 2
            resource_priority: 2
            tag_priority: 2
            resource_arn: "Foo"
            quadrant: "Foo"
        }
    ) {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Updating a single ReclassificationEvents

Single ReclassificationEvents update mutations take two inputs:

-   `where`: `ReclassificationEventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `ReclassificationEventsUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateReclassificationEvents(
        where: { id: 2 }
        data: {
            region: "Foo"
            source: "Foo"
            resource: "Foo"
            action: "Foo"
            state: "Foo"
            costly_resource_avg: 2
            resource_priority_avg: 2
            detail_type: "Foo"
            time: "dd/mm/YYYY"
            region_priority: 2
            service_priority: 2
            resource_priority: 2
            tag_priority: 2
            resource_arn: "Foo"
            quadrant: "Foo"
        }
    ) {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Deleting a single ReclassificationEvents

Single ReclassificationEvents delete mutations take one input:

-   `where`: `ReclassificationEventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteReclassificationEvents(where: { id: 2 }) {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Creating multiple ReclassificationEvents

Multiple ReclassificationEvents create mutations take one input:

-   `data`: `[ReclassificationEventsCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyReclassificationEvents(
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

> `createManyReclassificationEvents` returns an integer that represents the number of records that were created.

### Updating multiple ReclassificationEvents

Multiple ReclassificationEvents update mutations take two inputs:

-   `where`: `ReclassificationEventsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `ReclassificationEventsUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyReclassificationEvents(
        where: { region: "Foo" }
        data: { region: "Foo" }
    ) {
        count
    }
}
```

> `updateManyReclassificationEvents` returns an integer that represents the number of records that were updated.

### Deleting multiple ReclassificationEvents

Multiple ReclassificationEvents delete mutations can take one input:

-   `where`: `ReclassificationEventsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyReclassificationEvents(
        where: { region: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyReclassificationEvents` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single ReclassificationEvents creation

Triggered from `createReclassificationEvents` mutation (excl. `createManyReclassificationEvents` and `upsertReclassificationEvents`).

```graphql
subscription {
    onCreatedReclassificationEvents {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Subscribing to a single ReclassificationEvents update

Triggered from `updateReclassificationEvents` mutation (excl. `updateManyReclassificationEvents` and `upsertReclassificationEvents`).

```graphql
subscription {
    onUpdatedReclassificationEvents {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Subscribing to a single ReclassificationEvents upsert

Triggered from `upsertReclassificationEvents` mutation.

```graphql
subscription {
    onUpsertedReclassificationEvents {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Subscribing to a single ReclassificationEvents deletion

Triggered from `deleteReclassificationEvents` mutation (excl. `deleteManyReclassificationEvents`).

```graphql
subscription {
    onDeletedReclassificationEvents {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Subscribing to a single ReclassificationEvents mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyReclassificationEvents`).

```graphql
subscription {
    onMutatedReclassificationEvents {
        region
        source
        resource
        action
        state
        costly_resource_avg
        resource_priority_avg
        detail_type
        id
        time
        region_priority
        service_priority
        resource_priority
        tag_priority
        resource_arn
        quadrant
    }
}
```

### Subscribing to many ReclassificationEvents creations

Triggered from `createManyReclassificationEvents` mutation.

```graphql
subscription {
    onCreatedManyReclassificationEvents {
        count
    }
}
```

### Subscribing to many ReclassificationEvents updates

Triggered from `updateManyReclassificationEvents` mutation.

```graphql
subscription {
    onUpdatedManyReclassificationEvents {
        count
    }
}
```

### Subscribing to many ReclassificationEvents deletions

Triggered from `deleteManyReclassificationEvents` mutation.

```graphql
subscription {
    onDeletedManyReclassificationEvents {
        count
    }
}
```

### Subscribing to many ReclassificationEvents mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyReclassificationEvents {
        count
    }
}
```
