# DevopsResourcePrioritySsm

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePrioritySsm` type.

| Field                  | Scalar Type | Unique  | Required (create) |
| ---------------------- | ----------- | ------- | ----------------- |
| id                     | Int         | true    | true              |
| resource_id            | String      | _false_ | _false_           |
| resource_type          | String      | _false_ | _false_           |
| compliance_or_doc_type | String      | _false_ | _false_           |
| status                 | String      | _false_ | _false_           |
| priority               | String      | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsResourcePrioritySsm`: Read a single DevopsResourcePrioritySsm.
-   `listDevopsResourcePrioritySsms`: Read multiple DevopsResourcePrioritySsms.
-   `countDevopsResourcePrioritySsms`: Count all DevopsResourcePrioritySsms.

### Querying a single DevopsResourcePrioritySsm

Single DevopsResourcePrioritySsm queries take one input:

-   `where`: `DevopsResourcePrioritySsmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePrioritySsm(where: { id: 2 }) {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Querying multiple DevopsResourcePrioritySsms

Multiple DevopsResourcePrioritySsms queries can take four inputs:

-   `where`: `DevopsResourcePrioritySsmWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePrioritySsmOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePrioritySsms {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsResourcePrioritySsms(skip: 0, take: 25) {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsResourcePrioritySsms(
        where: { resource_id: { equals: "Foo" } }
    ) {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsResourcePrioritySsms(
        where: { resource_id: { not: { equals: "Foo" } } }
    ) {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsResourcePrioritySsms(
        orderBy: [
            { resource_id: DESC }
            { resource_type: ASC }
        ]
    ) {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Counting DevopsResourcePrioritySsms

Counting DevopsResourcePrioritySsms queries can take four inputs:

-   `where`: `DevopsResourcePrioritySsmWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePrioritySsmOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePrioritySsms
}
```

> `countDevopsResourcePrioritySsms` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePrioritySsm`: Create a single DevopsResourcePrioritySsm.
-   `updateDevopsResourcePrioritySsm`: Update a single DevopsResourcePrioritySsm.
-   `upsertDevopsResourcePrioritySsm`: Update existing OR create single DevopsResourcePrioritySsm.
-   `deleteDevopsResourcePrioritySsm`: Delete a single DevopsResourcePrioritySsm.
-   `createManyDevopsResourcePrioritySsms`: Create multiple DevopsResourcePrioritySsms.
-   `updateManyDevopsResourcePrioritySsms`: Update multiple DevopsResourcePrioritySsms.
-   `deleteManyDevopsResourcePrioritySsms`: Delete multiple DevopsResourcePrioritySsms.

### Creating a single DevopsResourcePrioritySsm

Single DevopsResourcePrioritySsm create mutations take one input:

-   `data`: `DevopsResourcePrioritySsmCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePrioritySsm(
        data: {
            resource_id: "Foo"
            resource_type: "Foo"
            compliance_or_doc_type: "Foo"
            status: "Foo"
            priority: Decimal
        }
    ) {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Updating a single DevopsResourcePrioritySsm

Single DevopsResourcePrioritySsm update mutations take two inputs:

-   `where`: `DevopsResourcePrioritySsmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePrioritySsmUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePrioritySsm(
        where: { id: 2 }
        data: {
            resource_id: "Foo"
            resource_type: "Foo"
            compliance_or_doc_type: "Foo"
            status: "Foo"
            priority: Decimal
        }
    ) {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Deleting a single DevopsResourcePrioritySsm

Single DevopsResourcePrioritySsm delete mutations take one input:

-   `where`: `DevopsResourcePrioritySsmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePrioritySsm(where: { id: 2 }) {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Creating multiple DevopsResourcePrioritySsms

Multiple DevopsResourcePrioritySsms create mutations take one input:

-   `data`: `[DevopsResourcePrioritySsmCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePrioritySsms(
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

> `createManyDevopsResourcePrioritySsms` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePrioritySsms

Multiple DevopsResourcePrioritySsms update mutations take two inputs:

-   `where`: `DevopsResourcePrioritySsmWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePrioritySsmUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePrioritySsms(
        where: { resource_id: "Foo" }
        data: { resource_id: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePrioritySsms` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePrioritySsms

Multiple DevopsResourcePrioritySsms delete mutations can take one input:

-   `where`: `DevopsResourcePrioritySsmWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePrioritySsms(
        where: { resource_id: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePrioritySsms` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePrioritySsm creation

Triggered from `createDevopsResourcePrioritySsm` mutation (excl. `createManyDevopsResourcePrioritySsms` and `upsertDevopsResourcePrioritySsm`).

```graphql
subscription {
    onCreatedDevopsResourcePrioritySsm {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Subscribing to a single DevopsResourcePrioritySsm update

Triggered from `updateDevopsResourcePrioritySsm` mutation (excl. `updateManyDevopsResourcePrioritySsms` and `upsertDevopsResourcePrioritySsm`).

```graphql
subscription {
    onUpdatedDevopsResourcePrioritySsm {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Subscribing to a single DevopsResourcePrioritySsm upsert

Triggered from `upsertDevopsResourcePrioritySsm` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePrioritySsm {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Subscribing to a single DevopsResourcePrioritySsm deletion

Triggered from `deleteDevopsResourcePrioritySsm` mutation (excl. `deleteManyDevopsResourcePrioritySsms`).

```graphql
subscription {
    onDeletedDevopsResourcePrioritySsm {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Subscribing to a single DevopsResourcePrioritySsm mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePrioritySsms`).

```graphql
subscription {
    onMutatedDevopsResourcePrioritySsm {
        id
        resource_id
        resource_type
        compliance_or_doc_type
        status
        priority
    }
}
```

### Subscribing to many DevopsResourcePrioritySsm creations

Triggered from `createManyDevopsResourcePrioritySsms` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePrioritySsms {
        count
    }
}
```

### Subscribing to many DevopsResourcePrioritySsm updates

Triggered from `updateManyDevopsResourcePrioritySsms` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePrioritySsms {
        count
    }
}
```

### Subscribing to many DevopsResourcePrioritySsm deletions

Triggered from `deleteManyDevopsResourcePrioritySsms` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePrioritySsms {
        count
    }
}
```

### Subscribing to many DevopsResourcePrioritySsm mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePrioritySsms {
        count
    }
}
```
