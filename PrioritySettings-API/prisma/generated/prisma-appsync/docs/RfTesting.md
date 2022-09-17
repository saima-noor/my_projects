# RfTesting

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `RfTesting` type.

| Field                 | Scalar Type | Unique  | Required (create) |
| --------------------- | ----------- | ------- | ----------------- |
| id                    | Int         | true    | true              |
| time                  | AWSDateTime | _false_ | _false_           |
| region                | String      | _false_ | _false_           |
| region_priority       | Int         | _false_ | _false_           |
| event_source          | String      | _false_ | _false_           |
| service_priority      | Int         | _false_ | _false_           |
| resource_name         | String      | _false_ | _false_           |
| resource_prioirty     | String      | _false_ | _false_           |
| resource_arn          | String      | _false_ | _false_           |
| the_event             | String      | _false_ | _false_           |
| event_state           | String      | _false_ | _false_           |
| costly_resource_value | Int         | _false_ | _false_           |
| tag_priority          | Int         | _false_ | _false_           |
| quadrant              | String      | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getRfTesting`: Read a single RfTesting.
-   `listRfTestings`: Read multiple RfTestings.
-   `countRfTestings`: Count all RfTestings.

### Querying a single RfTesting

Single RfTesting queries take one input:

-   `where`: `RfTestingWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getRfTesting(where: { id: 2 }) {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Querying multiple RfTestings

Multiple RfTestings queries can take four inputs:

-   `where`: `RfTestingWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[RfTestingOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listRfTestings {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listRfTestings(skip: 0, take: 25) {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listRfTestings(
        where: { time: { equals: "dd/mm/YYYY" } }
    ) {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listRfTestings(
        where: { time: { not: { equals: "dd/mm/YYYY" } } }
    ) {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listRfTestings(
        orderBy: [{ time: DESC }, { region: ASC }]
    ) {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Counting RfTestings

Counting RfTestings queries can take four inputs:

-   `where`: `RfTestingWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[RfTestingOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countRfTestings
}
```

> `countRfTestings` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createRfTesting`: Create a single RfTesting.
-   `updateRfTesting`: Update a single RfTesting.
-   `upsertRfTesting`: Update existing OR create single RfTesting.
-   `deleteRfTesting`: Delete a single RfTesting.
-   `createManyRfTestings`: Create multiple RfTestings.
-   `updateManyRfTestings`: Update multiple RfTestings.
-   `deleteManyRfTestings`: Delete multiple RfTestings.

### Creating a single RfTesting

Single RfTesting create mutations take one input:

-   `data`: `RfTestingCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createRfTesting(
        data: {
            time: "dd/mm/YYYY"
            region: "Foo"
            region_priority: 2
            event_source: "Foo"
            service_priority: 2
            resource_name: "Foo"
            resource_prioirty: "Foo"
            resource_arn: "Foo"
            the_event: "Foo"
            event_state: "Foo"
            costly_resource_value: 2
            tag_priority: 2
            quadrant: "Foo"
        }
    ) {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Updating a single RfTesting

Single RfTesting update mutations take two inputs:

-   `where`: `RfTestingWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `RfTestingUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateRfTesting(
        where: { id: 2 }
        data: {
            time: "dd/mm/YYYY"
            region: "Foo"
            region_priority: 2
            event_source: "Foo"
            service_priority: 2
            resource_name: "Foo"
            resource_prioirty: "Foo"
            resource_arn: "Foo"
            the_event: "Foo"
            event_state: "Foo"
            costly_resource_value: 2
            tag_priority: 2
            quadrant: "Foo"
        }
    ) {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Deleting a single RfTesting

Single RfTesting delete mutations take one input:

-   `where`: `RfTestingWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteRfTesting(where: { id: 2 }) {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Creating multiple RfTestings

Multiple RfTestings create mutations take one input:

-   `data`: `[RfTestingCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyRfTestings(
        data: [
            { time: "dd/mm/YYYY" }
            { time: "dd/mm/YYYY" }
            { time: "dd/mm/YYYY" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyRfTestings` returns an integer that represents the number of records that were created.

### Updating multiple RfTestings

Multiple RfTestings update mutations take two inputs:

-   `where`: `RfTestingWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `RfTestingUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyRfTestings(
        where: { time: "dd/mm/YYYY" }
        data: { time: "dd/mm/YYYY" }
    ) {
        count
    }
}
```

> `updateManyRfTestings` returns an integer that represents the number of records that were updated.

### Deleting multiple RfTestings

Multiple RfTestings delete mutations can take one input:

-   `where`: `RfTestingWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyRfTestings(where: { time: "dd/mm/YYYY" }) {
        count
    }
}
```

> `deleteManyRfTestings` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single RfTesting creation

Triggered from `createRfTesting` mutation (excl. `createManyRfTestings` and `upsertRfTesting`).

```graphql
subscription {
    onCreatedRfTesting {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Subscribing to a single RfTesting update

Triggered from `updateRfTesting` mutation (excl. `updateManyRfTestings` and `upsertRfTesting`).

```graphql
subscription {
    onUpdatedRfTesting {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Subscribing to a single RfTesting upsert

Triggered from `upsertRfTesting` mutation.

```graphql
subscription {
    onUpsertedRfTesting {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Subscribing to a single RfTesting deletion

Triggered from `deleteRfTesting` mutation (excl. `deleteManyRfTestings`).

```graphql
subscription {
    onDeletedRfTesting {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Subscribing to a single RfTesting mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyRfTestings`).

```graphql
subscription {
    onMutatedRfTesting {
        id
        time
        region
        region_priority
        event_source
        service_priority
        resource_name
        resource_prioirty
        resource_arn
        the_event
        event_state
        costly_resource_value
        tag_priority
        quadrant
    }
}
```

### Subscribing to many RfTesting creations

Triggered from `createManyRfTestings` mutation.

```graphql
subscription {
    onCreatedManyRfTestings {
        count
    }
}
```

### Subscribing to many RfTesting updates

Triggered from `updateManyRfTestings` mutation.

```graphql
subscription {
    onUpdatedManyRfTestings {
        count
    }
}
```

### Subscribing to many RfTesting deletions

Triggered from `deleteManyRfTestings` mutation.

```graphql
subscription {
    onDeletedManyRfTestings {
        count
    }
}
```

### Subscribing to many RfTesting mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyRfTestings {
        count
    }
}
```
