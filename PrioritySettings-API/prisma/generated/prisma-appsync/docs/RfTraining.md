# RfTraining

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `RfTraining` type.

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

-   `getRfTraining`: Read a single RfTraining.
-   `listRfTrainings`: Read multiple RfTrainings.
-   `countRfTrainings`: Count all RfTrainings.

### Querying a single RfTraining

Single RfTraining queries take one input:

-   `where`: `RfTrainingWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getRfTraining(where: { id: 2 }) {
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

### Querying multiple RfTrainings

Multiple RfTrainings queries can take four inputs:

-   `where`: `RfTrainingWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[RfTrainingOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listRfTrainings {
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
    listRfTrainings(skip: 0, take: 25) {
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
    listRfTrainings(
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
    listRfTrainings(
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
    listRfTrainings(
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

### Counting RfTrainings

Counting RfTrainings queries can take four inputs:

-   `where`: `RfTrainingWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[RfTrainingOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countRfTrainings
}
```

> `countRfTrainings` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createRfTraining`: Create a single RfTraining.
-   `updateRfTraining`: Update a single RfTraining.
-   `upsertRfTraining`: Update existing OR create single RfTraining.
-   `deleteRfTraining`: Delete a single RfTraining.
-   `createManyRfTrainings`: Create multiple RfTrainings.
-   `updateManyRfTrainings`: Update multiple RfTrainings.
-   `deleteManyRfTrainings`: Delete multiple RfTrainings.

### Creating a single RfTraining

Single RfTraining create mutations take one input:

-   `data`: `RfTrainingCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createRfTraining(
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

### Updating a single RfTraining

Single RfTraining update mutations take two inputs:

-   `where`: `RfTrainingWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `RfTrainingUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateRfTraining(
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

### Deleting a single RfTraining

Single RfTraining delete mutations take one input:

-   `where`: `RfTrainingWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteRfTraining(where: { id: 2 }) {
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

### Creating multiple RfTrainings

Multiple RfTrainings create mutations take one input:

-   `data`: `[RfTrainingCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyRfTrainings(
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

> `createManyRfTrainings` returns an integer that represents the number of records that were created.

### Updating multiple RfTrainings

Multiple RfTrainings update mutations take two inputs:

-   `where`: `RfTrainingWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `RfTrainingUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyRfTrainings(
        where: { time: "dd/mm/YYYY" }
        data: { time: "dd/mm/YYYY" }
    ) {
        count
    }
}
```

> `updateManyRfTrainings` returns an integer that represents the number of records that were updated.

### Deleting multiple RfTrainings

Multiple RfTrainings delete mutations can take one input:

-   `where`: `RfTrainingWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyRfTrainings(where: { time: "dd/mm/YYYY" }) {
        count
    }
}
```

> `deleteManyRfTrainings` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single RfTraining creation

Triggered from `createRfTraining` mutation (excl. `createManyRfTrainings` and `upsertRfTraining`).

```graphql
subscription {
    onCreatedRfTraining {
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

### Subscribing to a single RfTraining update

Triggered from `updateRfTraining` mutation (excl. `updateManyRfTrainings` and `upsertRfTraining`).

```graphql
subscription {
    onUpdatedRfTraining {
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

### Subscribing to a single RfTraining upsert

Triggered from `upsertRfTraining` mutation.

```graphql
subscription {
    onUpsertedRfTraining {
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

### Subscribing to a single RfTraining deletion

Triggered from `deleteRfTraining` mutation (excl. `deleteManyRfTrainings`).

```graphql
subscription {
    onDeletedRfTraining {
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

### Subscribing to a single RfTraining mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyRfTrainings`).

```graphql
subscription {
    onMutatedRfTraining {
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

### Subscribing to many RfTraining creations

Triggered from `createManyRfTrainings` mutation.

```graphql
subscription {
    onCreatedManyRfTrainings {
        count
    }
}
```

### Subscribing to many RfTraining updates

Triggered from `updateManyRfTrainings` mutation.

```graphql
subscription {
    onUpdatedManyRfTrainings {
        count
    }
}
```

### Subscribing to many RfTraining deletions

Triggered from `deleteManyRfTrainings` mutation.

```graphql
subscription {
    onDeletedManyRfTrainings {
        count
    }
}
```

### Subscribing to many RfTraining mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyRfTrainings {
        count
    }
}
```
