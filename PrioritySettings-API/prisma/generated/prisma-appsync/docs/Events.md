# Events

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `Events` type.

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

-   `getEvents`: Read a single Events.
-   `listEvents`: Read multiple Events.
-   `countEvents`: Count all Events.

### Querying a single Events

Single Events queries take one input:

-   `where`: `EventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getEvents(where: { id: 2 }) {
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

### Querying multiple Events

Multiple Events queries can take four inputs:

-   `where`: `EventsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[EventsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listEvents {
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
    listEvents(skip: 0, take: 25) {
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
    listEvents(where: { region: { equals: "Foo" } }) {
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
    listEvents(
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
    listEvents(
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

### Counting Events

Counting Events queries can take four inputs:

-   `where`: `EventsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[EventsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countEvents
}
```

> `countEvents` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createEvents`: Create a single Events.
-   `updateEvents`: Update a single Events.
-   `upsertEvents`: Update existing OR create single Events.
-   `deleteEvents`: Delete a single Events.
-   `createManyEvents`: Create multiple Events.
-   `updateManyEvents`: Update multiple Events.
-   `deleteManyEvents`: Delete multiple Events.

### Creating a single Events

Single Events create mutations take one input:

-   `data`: `EventsCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createEvents(
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

### Updating a single Events

Single Events update mutations take two inputs:

-   `where`: `EventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `EventsUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateEvents(
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

### Deleting a single Events

Single Events delete mutations take one input:

-   `where`: `EventsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteEvents(where: { id: 2 }) {
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

### Creating multiple Events

Multiple Events create mutations take one input:

-   `data`: `[EventsCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyEvents(
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

> `createManyEvents` returns an integer that represents the number of records that were created.

### Updating multiple Events

Multiple Events update mutations take two inputs:

-   `where`: `EventsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `EventsUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyEvents(
        where: { region: "Foo" }
        data: { region: "Foo" }
    ) {
        count
    }
}
```

> `updateManyEvents` returns an integer that represents the number of records that were updated.

### Deleting multiple Events

Multiple Events delete mutations can take one input:

-   `where`: `EventsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyEvents(where: { region: "Foo" }) {
        count
    }
}
```

> `deleteManyEvents` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single Events creation

Triggered from `createEvents` mutation (excl. `createManyEvents` and `upsertEvents`).

```graphql
subscription {
    onCreatedEvents {
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

### Subscribing to a single Events update

Triggered from `updateEvents` mutation (excl. `updateManyEvents` and `upsertEvents`).

```graphql
subscription {
    onUpdatedEvents {
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

### Subscribing to a single Events upsert

Triggered from `upsertEvents` mutation.

```graphql
subscription {
    onUpsertedEvents {
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

### Subscribing to a single Events deletion

Triggered from `deleteEvents` mutation (excl. `deleteManyEvents`).

```graphql
subscription {
    onDeletedEvents {
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

### Subscribing to a single Events mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyEvents`).

```graphql
subscription {
    onMutatedEvents {
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

### Subscribing to many Events creations

Triggered from `createManyEvents` mutation.

```graphql
subscription {
    onCreatedManyEvents {
        count
    }
}
```

### Subscribing to many Events updates

Triggered from `updateManyEvents` mutation.

```graphql
subscription {
    onUpdatedManyEvents {
        count
    }
}
```

### Subscribing to many Events deletions

Triggered from `deleteManyEvents` mutation.

```graphql
subscription {
    onDeletedManyEvents {
        count
    }
}
```

### Subscribing to many Events mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyEvents {
        count
    }
}
```
