# AwsDevopsServicesList

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `AwsDevopsServicesList` type.

| Field         | Scalar Type | Unique  | Required (create) |
| ------------- | ----------- | ------- | ----------------- |
| id            | Int         | true    | true              |
| service_name  | String      | _false_ | _false_           |
| resource_type | String      | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getAwsDevopsServicesList`: Read a single AwsDevopsServicesList.
-   `listAwsDevopsServicesLists`: Read multiple AwsDevopsServicesLists.
-   `countAwsDevopsServicesLists`: Count all AwsDevopsServicesLists.

### Querying a single AwsDevopsServicesList

Single AwsDevopsServicesList queries take one input:

-   `where`: `AwsDevopsServicesListWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getAwsDevopsServicesList(where: { id: 2 }) {
        id
        service_name
        resource_type
    }
}
```

### Querying multiple AwsDevopsServicesLists

Multiple AwsDevopsServicesLists queries can take four inputs:

-   `where`: `AwsDevopsServicesListWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[AwsDevopsServicesListOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listAwsDevopsServicesLists {
        id
        service_name
        resource_type
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listAwsDevopsServicesLists(skip: 0, take: 25) {
        id
        service_name
        resource_type
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listAwsDevopsServicesLists(
        where: { service_name: { equals: "Foo" } }
    ) {
        id
        service_name
        resource_type
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listAwsDevopsServicesLists(
        where: { service_name: { not: { equals: "Foo" } } }
    ) {
        id
        service_name
        resource_type
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listAwsDevopsServicesLists(
        orderBy: [
            { service_name: DESC }
            { resource_type: ASC }
        ]
    ) {
        id
        service_name
        resource_type
    }
}
```

### Counting AwsDevopsServicesLists

Counting AwsDevopsServicesLists queries can take four inputs:

-   `where`: `AwsDevopsServicesListWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[AwsDevopsServicesListOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countAwsDevopsServicesLists
}
```

> `countAwsDevopsServicesLists` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createAwsDevopsServicesList`: Create a single AwsDevopsServicesList.
-   `updateAwsDevopsServicesList`: Update a single AwsDevopsServicesList.
-   `upsertAwsDevopsServicesList`: Update existing OR create single AwsDevopsServicesList.
-   `deleteAwsDevopsServicesList`: Delete a single AwsDevopsServicesList.
-   `createManyAwsDevopsServicesLists`: Create multiple AwsDevopsServicesLists.
-   `updateManyAwsDevopsServicesLists`: Update multiple AwsDevopsServicesLists.
-   `deleteManyAwsDevopsServicesLists`: Delete multiple AwsDevopsServicesLists.

### Creating a single AwsDevopsServicesList

Single AwsDevopsServicesList create mutations take one input:

-   `data`: `AwsDevopsServicesListCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createAwsDevopsServicesList(
        data: { service_name: "Foo", resource_type: "Foo" }
    ) {
        id
        service_name
        resource_type
    }
}
```

### Updating a single AwsDevopsServicesList

Single AwsDevopsServicesList update mutations take two inputs:

-   `where`: `AwsDevopsServicesListWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `AwsDevopsServicesListUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateAwsDevopsServicesList(
        where: { id: 2 }
        data: { service_name: "Foo", resource_type: "Foo" }
    ) {
        id
        service_name
        resource_type
    }
}
```

### Deleting a single AwsDevopsServicesList

Single AwsDevopsServicesList delete mutations take one input:

-   `where`: `AwsDevopsServicesListWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteAwsDevopsServicesList(where: { id: 2 }) {
        id
        service_name
        resource_type
    }
}
```

### Creating multiple AwsDevopsServicesLists

Multiple AwsDevopsServicesLists create mutations take one input:

-   `data`: `[AwsDevopsServicesListCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyAwsDevopsServicesLists(
        data: [
            { service_name: "Foo" }
            { service_name: "Foo" }
            { service_name: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyAwsDevopsServicesLists` returns an integer that represents the number of records that were created.

### Updating multiple AwsDevopsServicesLists

Multiple AwsDevopsServicesLists update mutations take two inputs:

-   `where`: `AwsDevopsServicesListWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `AwsDevopsServicesListUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyAwsDevopsServicesLists(
        where: { service_name: "Foo" }
        data: { service_name: "Foo" }
    ) {
        count
    }
}
```

> `updateManyAwsDevopsServicesLists` returns an integer that represents the number of records that were updated.

### Deleting multiple AwsDevopsServicesLists

Multiple AwsDevopsServicesLists delete mutations can take one input:

-   `where`: `AwsDevopsServicesListWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyAwsDevopsServicesLists(
        where: { service_name: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyAwsDevopsServicesLists` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single AwsDevopsServicesList creation

Triggered from `createAwsDevopsServicesList` mutation (excl. `createManyAwsDevopsServicesLists` and `upsertAwsDevopsServicesList`).

```graphql
subscription {
    onCreatedAwsDevopsServicesList {
        id
        service_name
        resource_type
    }
}
```

### Subscribing to a single AwsDevopsServicesList update

Triggered from `updateAwsDevopsServicesList` mutation (excl. `updateManyAwsDevopsServicesLists` and `upsertAwsDevopsServicesList`).

```graphql
subscription {
    onUpdatedAwsDevopsServicesList {
        id
        service_name
        resource_type
    }
}
```

### Subscribing to a single AwsDevopsServicesList upsert

Triggered from `upsertAwsDevopsServicesList` mutation.

```graphql
subscription {
    onUpsertedAwsDevopsServicesList {
        id
        service_name
        resource_type
    }
}
```

### Subscribing to a single AwsDevopsServicesList deletion

Triggered from `deleteAwsDevopsServicesList` mutation (excl. `deleteManyAwsDevopsServicesLists`).

```graphql
subscription {
    onDeletedAwsDevopsServicesList {
        id
        service_name
        resource_type
    }
}
```

### Subscribing to a single AwsDevopsServicesList mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyAwsDevopsServicesLists`).

```graphql
subscription {
    onMutatedAwsDevopsServicesList {
        id
        service_name
        resource_type
    }
}
```

### Subscribing to many AwsDevopsServicesList creations

Triggered from `createManyAwsDevopsServicesLists` mutation.

```graphql
subscription {
    onCreatedManyAwsDevopsServicesLists {
        count
    }
}
```

### Subscribing to many AwsDevopsServicesList updates

Triggered from `updateManyAwsDevopsServicesLists` mutation.

```graphql
subscription {
    onUpdatedManyAwsDevopsServicesLists {
        count
    }
}
```

### Subscribing to many AwsDevopsServicesList deletions

Triggered from `deleteManyAwsDevopsServicesLists` mutation.

```graphql
subscription {
    onDeletedManyAwsDevopsServicesLists {
        count
    }
}
```

### Subscribing to many AwsDevopsServicesList mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyAwsDevopsServicesLists {
        count
    }
}
```
