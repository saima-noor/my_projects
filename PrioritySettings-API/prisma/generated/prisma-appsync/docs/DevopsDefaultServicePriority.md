# DevopsDefaultServicePriority

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsDefaultServicePriority` type.

| Field            | Scalar Type | Unique  | Required (create) |
| ---------------- | ----------- | ------- | ----------------- |
| id               | Int         | true    | true              |
| resource_type    | String      | true    | _false_           |
| count            | Int         | _false_ | _false_           |
| service_priority | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsDefaultServicePriority`: Read a single DevopsDefaultServicePriority.
-   `listDevopsDefaultServicePriorities`: Read multiple DevopsDefaultServicePriorities.
-   `countDevopsDefaultServicePriorities`: Count all DevopsDefaultServicePriorities.

### Querying a single DevopsDefaultServicePriority

Single DevopsDefaultServicePriority queries take one input:

-   `where`: `DevopsDefaultServicePriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsDefaultServicePriority(where: { id: 2 }) {
        id
        resource_type
        count
        service_priority
    }
}
```

### Querying multiple DevopsDefaultServicePriorities

Multiple DevopsDefaultServicePriorities queries can take four inputs:

-   `where`: `DevopsDefaultServicePriorityWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsDefaultServicePriorityOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsDefaultServicePriorities {
        id
        resource_type
        count
        service_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsDefaultServicePriorities(skip: 0, take: 25) {
        id
        resource_type
        count
        service_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsDefaultServicePriorities(
        where: { count: { equals: 2 } }
    ) {
        id
        resource_type
        count
        service_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsDefaultServicePriorities(
        where: { count: { not: { equals: 2 } } }
    ) {
        id
        resource_type
        count
        service_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsDefaultServicePriorities(
        orderBy: [
            { count: DESC }
            { service_priority: ASC }
        ]
    ) {
        id
        resource_type
        count
        service_priority
    }
}
```

### Counting DevopsDefaultServicePriorities

Counting DevopsDefaultServicePriorities queries can take four inputs:

-   `where`: `DevopsDefaultServicePriorityWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsDefaultServicePriorityOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsDefaultServicePriorities
}
```

> `countDevopsDefaultServicePriorities` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsDefaultServicePriority`: Create a single DevopsDefaultServicePriority.
-   `updateDevopsDefaultServicePriority`: Update a single DevopsDefaultServicePriority.
-   `upsertDevopsDefaultServicePriority`: Update existing OR create single DevopsDefaultServicePriority.
-   `deleteDevopsDefaultServicePriority`: Delete a single DevopsDefaultServicePriority.
-   `createManyDevopsDefaultServicePriorities`: Create multiple DevopsDefaultServicePriorities.
-   `updateManyDevopsDefaultServicePriorities`: Update multiple DevopsDefaultServicePriorities.
-   `deleteManyDevopsDefaultServicePriorities`: Delete multiple DevopsDefaultServicePriorities.

### Creating a single DevopsDefaultServicePriority

Single DevopsDefaultServicePriority create mutations take one input:

-   `data`: `DevopsDefaultServicePriorityCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsDefaultServicePriority(
        data: {
            resource_type: "Foo"
            count: 2
            service_priority: 2
        }
    ) {
        id
        resource_type
        count
        service_priority
    }
}
```

### Updating a single DevopsDefaultServicePriority

Single DevopsDefaultServicePriority update mutations take two inputs:

-   `where`: `DevopsDefaultServicePriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsDefaultServicePriorityUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsDefaultServicePriority(
        where: { id: 2 }
        data: {
            resource_type: "Foo"
            count: 2
            service_priority: 2
        }
    ) {
        id
        resource_type
        count
        service_priority
    }
}
```

### Deleting a single DevopsDefaultServicePriority

Single DevopsDefaultServicePriority delete mutations take one input:

-   `where`: `DevopsDefaultServicePriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsDefaultServicePriority(where: { id: 2 }) {
        id
        resource_type
        count
        service_priority
    }
}
```

### Creating multiple DevopsDefaultServicePriorities

Multiple DevopsDefaultServicePriorities create mutations take one input:

-   `data`: `[DevopsDefaultServicePriorityCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsDefaultServicePriorities(
        data: [{ count: 2 }, { count: 2 }, { count: 2 }]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsDefaultServicePriorities` returns an integer that represents the number of records that were created.

### Updating multiple DevopsDefaultServicePriorities

Multiple DevopsDefaultServicePriorities update mutations take two inputs:

-   `where`: `DevopsDefaultServicePriorityWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsDefaultServicePriorityUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsDefaultServicePriorities(
        where: { count: 2 }
        data: { count: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsDefaultServicePriorities` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsDefaultServicePriorities

Multiple DevopsDefaultServicePriorities delete mutations can take one input:

-   `where`: `DevopsDefaultServicePriorityWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsDefaultServicePriorities(
        where: { count: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsDefaultServicePriorities` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsDefaultServicePriority creation

Triggered from `createDevopsDefaultServicePriority` mutation (excl. `createManyDevopsDefaultServicePriorities` and `upsertDevopsDefaultServicePriority`).

```graphql
subscription {
    onCreatedDevopsDefaultServicePriority {
        id
        resource_type
        count
        service_priority
    }
}
```

### Subscribing to a single DevopsDefaultServicePriority update

Triggered from `updateDevopsDefaultServicePriority` mutation (excl. `updateManyDevopsDefaultServicePriorities` and `upsertDevopsDefaultServicePriority`).

```graphql
subscription {
    onUpdatedDevopsDefaultServicePriority {
        id
        resource_type
        count
        service_priority
    }
}
```

### Subscribing to a single DevopsDefaultServicePriority upsert

Triggered from `upsertDevopsDefaultServicePriority` mutation.

```graphql
subscription {
    onUpsertedDevopsDefaultServicePriority {
        id
        resource_type
        count
        service_priority
    }
}
```

### Subscribing to a single DevopsDefaultServicePriority deletion

Triggered from `deleteDevopsDefaultServicePriority` mutation (excl. `deleteManyDevopsDefaultServicePriorities`).

```graphql
subscription {
    onDeletedDevopsDefaultServicePriority {
        id
        resource_type
        count
        service_priority
    }
}
```

### Subscribing to a single DevopsDefaultServicePriority mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsDefaultServicePriorities`).

```graphql
subscription {
    onMutatedDevopsDefaultServicePriority {
        id
        resource_type
        count
        service_priority
    }
}
```

### Subscribing to many DevopsDefaultServicePriority creations

Triggered from `createManyDevopsDefaultServicePriorities` mutation.

```graphql
subscription {
    onCreatedManyDevopsDefaultServicePriorities {
        count
    }
}
```

### Subscribing to many DevopsDefaultServicePriority updates

Triggered from `updateManyDevopsDefaultServicePriorities` mutation.

```graphql
subscription {
    onUpdatedManyDevopsDefaultServicePriorities {
        count
    }
}
```

### Subscribing to many DevopsDefaultServicePriority deletions

Triggered from `deleteManyDevopsDefaultServicePriorities` mutation.

```graphql
subscription {
    onDeletedManyDevopsDefaultServicePriorities {
        count
    }
}
```

### Subscribing to many DevopsDefaultServicePriority mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsDefaultServicePriorities {
        count
    }
}
```
