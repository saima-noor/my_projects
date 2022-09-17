# DevopsCostlyResourceCodecommit

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceCodecommit` type.

| Field               | Scalar Type | Unique  | Required (create) |
| ------------------- | ----------- | ------- | ----------------- |
| id                  | Int         | true    | true              |
| repository_id       | String      | _false_ | _false_           |
| repository_name     | String      | _false_ | _false_           |
| pull_requests       | Int         | _false_ | _false_           |
| pull_request_events | Int         | _false_ | _false_           |
| content_length      | Int         | _false_ | _false_           |
| priority            | String      | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceCodecommit`: Read a single DevopsCostlyResourceCodecommit.
-   `listDevopsCostlyResourceCodecommits`: Read multiple DevopsCostlyResourceCodecommits.
-   `countDevopsCostlyResourceCodecommits`: Count all DevopsCostlyResourceCodecommits.

### Querying a single DevopsCostlyResourceCodecommit

Single DevopsCostlyResourceCodecommit queries take one input:

-   `where`: `DevopsCostlyResourceCodecommitWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceCodecommit(where: { id: 2 }) {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Querying multiple DevopsCostlyResourceCodecommits

Multiple DevopsCostlyResourceCodecommits queries can take four inputs:

-   `where`: `DevopsCostlyResourceCodecommitWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceCodecommitOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceCodecommits {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsCostlyResourceCodecommits(skip: 0, take: 25) {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsCostlyResourceCodecommits(
        where: { repository_id: { equals: "Foo" } }
    ) {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsCostlyResourceCodecommits(
        where: { repository_id: { not: { equals: "Foo" } } }
    ) {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsCostlyResourceCodecommits(
        orderBy: [
            { repository_id: DESC }
            { repository_name: ASC }
        ]
    ) {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Counting DevopsCostlyResourceCodecommits

Counting DevopsCostlyResourceCodecommits queries can take four inputs:

-   `where`: `DevopsCostlyResourceCodecommitWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceCodecommitOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceCodecommits
}
```

> `countDevopsCostlyResourceCodecommits` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceCodecommit`: Create a single DevopsCostlyResourceCodecommit.
-   `updateDevopsCostlyResourceCodecommit`: Update a single DevopsCostlyResourceCodecommit.
-   `upsertDevopsCostlyResourceCodecommit`: Update existing OR create single DevopsCostlyResourceCodecommit.
-   `deleteDevopsCostlyResourceCodecommit`: Delete a single DevopsCostlyResourceCodecommit.
-   `createManyDevopsCostlyResourceCodecommits`: Create multiple DevopsCostlyResourceCodecommits.
-   `updateManyDevopsCostlyResourceCodecommits`: Update multiple DevopsCostlyResourceCodecommits.
-   `deleteManyDevopsCostlyResourceCodecommits`: Delete multiple DevopsCostlyResourceCodecommits.

### Creating a single DevopsCostlyResourceCodecommit

Single DevopsCostlyResourceCodecommit create mutations take one input:

-   `data`: `DevopsCostlyResourceCodecommitCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceCodecommit(
        data: {
            repository_id: "Foo"
            repository_name: "Foo"
            pull_requests: 2
            pull_request_events: 2
            content_length: 2
            priority: Decimal
        }
    ) {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Updating a single DevopsCostlyResourceCodecommit

Single DevopsCostlyResourceCodecommit update mutations take two inputs:

-   `where`: `DevopsCostlyResourceCodecommitWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceCodecommitUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceCodecommit(
        where: { id: 2 }
        data: {
            repository_id: "Foo"
            repository_name: "Foo"
            pull_requests: 2
            pull_request_events: 2
            content_length: 2
            priority: Decimal
        }
    ) {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Deleting a single DevopsCostlyResourceCodecommit

Single DevopsCostlyResourceCodecommit delete mutations take one input:

-   `where`: `DevopsCostlyResourceCodecommitWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceCodecommit(where: { id: 2 }) {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Creating multiple DevopsCostlyResourceCodecommits

Multiple DevopsCostlyResourceCodecommits create mutations take one input:

-   `data`: `[DevopsCostlyResourceCodecommitCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceCodecommits(
        data: [
            { repository_id: "Foo" }
            { repository_id: "Foo" }
            { repository_id: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsCostlyResourceCodecommits` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceCodecommits

Multiple DevopsCostlyResourceCodecommits update mutations take two inputs:

-   `where`: `DevopsCostlyResourceCodecommitWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceCodecommitUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceCodecommits(
        where: { repository_id: "Foo" }
        data: { repository_id: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceCodecommits` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceCodecommits

Multiple DevopsCostlyResourceCodecommits delete mutations can take one input:

-   `where`: `DevopsCostlyResourceCodecommitWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceCodecommits(
        where: { repository_id: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceCodecommits` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceCodecommit creation

Triggered from `createDevopsCostlyResourceCodecommit` mutation (excl. `createManyDevopsCostlyResourceCodecommits` and `upsertDevopsCostlyResourceCodecommit`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceCodecommit {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodecommit update

Triggered from `updateDevopsCostlyResourceCodecommit` mutation (excl. `updateManyDevopsCostlyResourceCodecommits` and `upsertDevopsCostlyResourceCodecommit`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceCodecommit {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodecommit upsert

Triggered from `upsertDevopsCostlyResourceCodecommit` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceCodecommit {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodecommit deletion

Triggered from `deleteDevopsCostlyResourceCodecommit` mutation (excl. `deleteManyDevopsCostlyResourceCodecommits`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceCodecommit {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodecommit mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceCodecommits`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceCodecommit {
        id
        repository_id
        repository_name
        pull_requests
        pull_request_events
        content_length
        priority
    }
}
```

### Subscribing to many DevopsCostlyResourceCodecommit creations

Triggered from `createManyDevopsCostlyResourceCodecommits` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceCodecommits {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodecommit updates

Triggered from `updateManyDevopsCostlyResourceCodecommits` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceCodecommits {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodecommit deletions

Triggered from `deleteManyDevopsCostlyResourceCodecommits` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceCodecommits {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodecommit mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceCodecommits {
        count
    }
}
```
