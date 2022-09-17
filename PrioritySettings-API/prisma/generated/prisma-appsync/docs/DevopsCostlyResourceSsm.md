# DevopsCostlyResourceSsm

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceSsm` type.

| Field                | Scalar Type | Unique  | Required (create) |
| -------------------- | ----------- | ------- | ----------------- |
| id                   | Int         | true    | true              |
| resource_id          | String      | _false_ | _false_           |
| resource_type        | String      | _false_ | _false_           |
| followed_action_type | String      | _false_ | _false_           |
| status               | String      | _false_ | _false_           |
| costly_priority      | String      | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceSsm`: Read a single DevopsCostlyResourceSsm.
-   `listDevopsCostlyResourceSsms`: Read multiple DevopsCostlyResourceSsms.
-   `countDevopsCostlyResourceSsms`: Count all DevopsCostlyResourceSsms.

### Querying a single DevopsCostlyResourceSsm

Single DevopsCostlyResourceSsm queries take one input:

-   `where`: `DevopsCostlyResourceSsmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceSsm(where: { id: 2 }) {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Querying multiple DevopsCostlyResourceSsms

Multiple DevopsCostlyResourceSsms queries can take four inputs:

-   `where`: `DevopsCostlyResourceSsmWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceSsmOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceSsms {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsCostlyResourceSsms(skip: 0, take: 25) {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsCostlyResourceSsms(
        where: { resource_id: { equals: "Foo" } }
    ) {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsCostlyResourceSsms(
        where: { resource_id: { not: { equals: "Foo" } } }
    ) {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsCostlyResourceSsms(
        orderBy: [
            { resource_id: DESC }
            { resource_type: ASC }
        ]
    ) {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Counting DevopsCostlyResourceSsms

Counting DevopsCostlyResourceSsms queries can take four inputs:

-   `where`: `DevopsCostlyResourceSsmWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceSsmOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceSsms
}
```

> `countDevopsCostlyResourceSsms` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceSsm`: Create a single DevopsCostlyResourceSsm.
-   `updateDevopsCostlyResourceSsm`: Update a single DevopsCostlyResourceSsm.
-   `upsertDevopsCostlyResourceSsm`: Update existing OR create single DevopsCostlyResourceSsm.
-   `deleteDevopsCostlyResourceSsm`: Delete a single DevopsCostlyResourceSsm.
-   `createManyDevopsCostlyResourceSsms`: Create multiple DevopsCostlyResourceSsms.
-   `updateManyDevopsCostlyResourceSsms`: Update multiple DevopsCostlyResourceSsms.
-   `deleteManyDevopsCostlyResourceSsms`: Delete multiple DevopsCostlyResourceSsms.

### Creating a single DevopsCostlyResourceSsm

Single DevopsCostlyResourceSsm create mutations take one input:

-   `data`: `DevopsCostlyResourceSsmCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceSsm(
        data: {
            resource_id: "Foo"
            resource_type: "Foo"
            followed_action_type: "Foo"
            status: "Foo"
            costly_priority: "Foo"
        }
    ) {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Updating a single DevopsCostlyResourceSsm

Single DevopsCostlyResourceSsm update mutations take two inputs:

-   `where`: `DevopsCostlyResourceSsmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceSsmUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceSsm(
        where: { id: 2 }
        data: {
            resource_id: "Foo"
            resource_type: "Foo"
            followed_action_type: "Foo"
            status: "Foo"
            costly_priority: "Foo"
        }
    ) {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Deleting a single DevopsCostlyResourceSsm

Single DevopsCostlyResourceSsm delete mutations take one input:

-   `where`: `DevopsCostlyResourceSsmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceSsm(where: { id: 2 }) {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Creating multiple DevopsCostlyResourceSsms

Multiple DevopsCostlyResourceSsms create mutations take one input:

-   `data`: `[DevopsCostlyResourceSsmCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceSsms(
        data: [
            { resource_id: "Foo" }
            { resource_id: "Foo" }
            { resource_id: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsCostlyResourceSsms` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceSsms

Multiple DevopsCostlyResourceSsms update mutations take two inputs:

-   `where`: `DevopsCostlyResourceSsmWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceSsmUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceSsms(
        where: { resource_id: "Foo" }
        data: { resource_id: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceSsms` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceSsms

Multiple DevopsCostlyResourceSsms delete mutations can take one input:

-   `where`: `DevopsCostlyResourceSsmWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceSsms(
        where: { resource_id: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceSsms` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceSsm creation

Triggered from `createDevopsCostlyResourceSsm` mutation (excl. `createManyDevopsCostlyResourceSsms` and `upsertDevopsCostlyResourceSsm`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceSsm {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceSsm update

Triggered from `updateDevopsCostlyResourceSsm` mutation (excl. `updateManyDevopsCostlyResourceSsms` and `upsertDevopsCostlyResourceSsm`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceSsm {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceSsm upsert

Triggered from `upsertDevopsCostlyResourceSsm` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceSsm {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceSsm deletion

Triggered from `deleteDevopsCostlyResourceSsm` mutation (excl. `deleteManyDevopsCostlyResourceSsms`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceSsm {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceSsm mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceSsms`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceSsm {
        id
        resource_id
        resource_type
        followed_action_type
        status
        costly_priority
    }
}
```

### Subscribing to many DevopsCostlyResourceSsm creations

Triggered from `createManyDevopsCostlyResourceSsms` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceSsms {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceSsm updates

Triggered from `updateManyDevopsCostlyResourceSsms` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceSsms {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceSsm deletions

Triggered from `deleteManyDevopsCostlyResourceSsms` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceSsms {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceSsm mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceSsms {
        count
    }
}
```
