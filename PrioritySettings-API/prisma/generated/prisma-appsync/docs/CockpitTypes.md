# CockpitTypes

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `CockpitTypes` type.

| Field        | Scalar Type | Unique  | Required (create) |
| ------------ | ----------- | ------- | ----------------- |
| id           | Int         | true    | true              |
| cockpit_id   | String      | _false_ | _false_           |
| cockpit_name | String      | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getCockpitTypes`: Read a single CockpitTypes.
-   `listCockpitTypes`: Read multiple CockpitTypes.
-   `countCockpitTypes`: Count all CockpitTypes.

### Querying a single CockpitTypes

Single CockpitTypes queries take one input:

-   `where`: `CockpitTypesWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getCockpitTypes(where: { id: 2 }) {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Querying multiple CockpitTypes

Multiple CockpitTypes queries can take four inputs:

-   `where`: `CockpitTypesWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[CockpitTypesOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listCockpitTypes {
        id
        cockpit_id
        cockpit_name
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listCockpitTypes(skip: 0, take: 25) {
        id
        cockpit_id
        cockpit_name
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listCockpitTypes(
        where: { cockpit_id: { equals: "Foo" } }
    ) {
        id
        cockpit_id
        cockpit_name
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listCockpitTypes(
        where: { cockpit_id: { not: { equals: "Foo" } } }
    ) {
        id
        cockpit_id
        cockpit_name
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listCockpitTypes(
        orderBy: [
            { cockpit_id: DESC }
            { cockpit_name: ASC }
        ]
    ) {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Counting CockpitTypes

Counting CockpitTypes queries can take four inputs:

-   `where`: `CockpitTypesWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[CockpitTypesOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countCockpitTypes
}
```

> `countCockpitTypes` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createCockpitTypes`: Create a single CockpitTypes.
-   `updateCockpitTypes`: Update a single CockpitTypes.
-   `upsertCockpitTypes`: Update existing OR create single CockpitTypes.
-   `deleteCockpitTypes`: Delete a single CockpitTypes.
-   `createManyCockpitTypes`: Create multiple CockpitTypes.
-   `updateManyCockpitTypes`: Update multiple CockpitTypes.
-   `deleteManyCockpitTypes`: Delete multiple CockpitTypes.

### Creating a single CockpitTypes

Single CockpitTypes create mutations take one input:

-   `data`: `CockpitTypesCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createCockpitTypes(
        data: { cockpit_id: "Foo", cockpit_name: "Foo" }
    ) {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Updating a single CockpitTypes

Single CockpitTypes update mutations take two inputs:

-   `where`: `CockpitTypesWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `CockpitTypesUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateCockpitTypes(
        where: { id: 2 }
        data: { cockpit_id: "Foo", cockpit_name: "Foo" }
    ) {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Deleting a single CockpitTypes

Single CockpitTypes delete mutations take one input:

-   `where`: `CockpitTypesWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteCockpitTypes(where: { id: 2 }) {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Creating multiple CockpitTypes

Multiple CockpitTypes create mutations take one input:

-   `data`: `[CockpitTypesCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyCockpitTypes(
        data: [
            { cockpit_id: "Foo" }
            { cockpit_id: "Foo" }
            { cockpit_id: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyCockpitTypes` returns an integer that represents the number of records that were created.

### Updating multiple CockpitTypes

Multiple CockpitTypes update mutations take two inputs:

-   `where`: `CockpitTypesWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `CockpitTypesUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyCockpitTypes(
        where: { cockpit_id: "Foo" }
        data: { cockpit_id: "Foo" }
    ) {
        count
    }
}
```

> `updateManyCockpitTypes` returns an integer that represents the number of records that were updated.

### Deleting multiple CockpitTypes

Multiple CockpitTypes delete mutations can take one input:

-   `where`: `CockpitTypesWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyCockpitTypes(where: { cockpit_id: "Foo" }) {
        count
    }
}
```

> `deleteManyCockpitTypes` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single CockpitTypes creation

Triggered from `createCockpitTypes` mutation (excl. `createManyCockpitTypes` and `upsertCockpitTypes`).

```graphql
subscription {
    onCreatedCockpitTypes {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Subscribing to a single CockpitTypes update

Triggered from `updateCockpitTypes` mutation (excl. `updateManyCockpitTypes` and `upsertCockpitTypes`).

```graphql
subscription {
    onUpdatedCockpitTypes {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Subscribing to a single CockpitTypes upsert

Triggered from `upsertCockpitTypes` mutation.

```graphql
subscription {
    onUpsertedCockpitTypes {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Subscribing to a single CockpitTypes deletion

Triggered from `deleteCockpitTypes` mutation (excl. `deleteManyCockpitTypes`).

```graphql
subscription {
    onDeletedCockpitTypes {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Subscribing to a single CockpitTypes mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyCockpitTypes`).

```graphql
subscription {
    onMutatedCockpitTypes {
        id
        cockpit_id
        cockpit_name
    }
}
```

### Subscribing to many CockpitTypes creations

Triggered from `createManyCockpitTypes` mutation.

```graphql
subscription {
    onCreatedManyCockpitTypes {
        count
    }
}
```

### Subscribing to many CockpitTypes updates

Triggered from `updateManyCockpitTypes` mutation.

```graphql
subscription {
    onUpdatedManyCockpitTypes {
        count
    }
}
```

### Subscribing to many CockpitTypes deletions

Triggered from `deleteManyCockpitTypes` mutation.

```graphql
subscription {
    onDeletedManyCockpitTypes {
        count
    }
}
```

### Subscribing to many CockpitTypes mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyCockpitTypes {
        count
    }
}
```
