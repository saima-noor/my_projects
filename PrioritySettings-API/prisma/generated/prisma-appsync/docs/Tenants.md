# Tenants

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `Tenants` type.

| Field             | Scalar Type | Unique  | Required (create) |
| ----------------- | ----------- | ------- | ----------------- |
| id                | Int         | true    | true              |
| tenant_id         | String      | _false_ | _false_           |
| email             | AWSEmail    | _false_ | _false_           |
| status            | String      | _false_ | _false_           |
| subscription_type | String      | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getTenants`: Read a single Tenants.
-   `listTenants`: Read multiple Tenants.
-   `countTenants`: Count all Tenants.

### Querying a single Tenants

Single Tenants queries take one input:

-   `where`: `TenantsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getTenants(where: { id: 2 }) {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Querying multiple Tenants

Multiple Tenants queries can take four inputs:

-   `where`: `TenantsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[TenantsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listTenants {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listTenants(skip: 0, take: 25) {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listTenants(where: { tenant_id: { equals: "Foo" } }) {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listTenants(
        where: { tenant_id: { not: { equals: "Foo" } } }
    ) {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listTenants(
        orderBy: [{ tenant_id: DESC }, { email: ASC }]
    ) {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Counting Tenants

Counting Tenants queries can take four inputs:

-   `where`: `TenantsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[TenantsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countTenants
}
```

> `countTenants` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createTenants`: Create a single Tenants.
-   `updateTenants`: Update a single Tenants.
-   `upsertTenants`: Update existing OR create single Tenants.
-   `deleteTenants`: Delete a single Tenants.
-   `createManyTenants`: Create multiple Tenants.
-   `updateManyTenants`: Update multiple Tenants.
-   `deleteManyTenants`: Delete multiple Tenants.

### Creating a single Tenants

Single Tenants create mutations take one input:

-   `data`: `TenantsCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createTenants(
        data: {
            tenant_id: "Foo"
            email: "Foo"
            status: "Foo"
            subscription_type: "Foo"
        }
    ) {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Updating a single Tenants

Single Tenants update mutations take two inputs:

-   `where`: `TenantsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `TenantsUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateTenants(
        where: { id: 2 }
        data: {
            tenant_id: "Foo"
            email: "Foo"
            status: "Foo"
            subscription_type: "Foo"
        }
    ) {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Deleting a single Tenants

Single Tenants delete mutations take one input:

-   `where`: `TenantsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteTenants(where: { id: 2 }) {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Creating multiple Tenants

Multiple Tenants create mutations take one input:

-   `data`: `[TenantsCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyTenants(
        data: [
            { tenant_id: "Foo" }
            { tenant_id: "Foo" }
            { tenant_id: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyTenants` returns an integer that represents the number of records that were created.

### Updating multiple Tenants

Multiple Tenants update mutations take two inputs:

-   `where`: `TenantsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `TenantsUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyTenants(
        where: { tenant_id: "Foo" }
        data: { tenant_id: "Foo" }
    ) {
        count
    }
}
```

> `updateManyTenants` returns an integer that represents the number of records that were updated.

### Deleting multiple Tenants

Multiple Tenants delete mutations can take one input:

-   `where`: `TenantsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyTenants(where: { tenant_id: "Foo" }) {
        count
    }
}
```

> `deleteManyTenants` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single Tenants creation

Triggered from `createTenants` mutation (excl. `createManyTenants` and `upsertTenants`).

```graphql
subscription {
    onCreatedTenants {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Subscribing to a single Tenants update

Triggered from `updateTenants` mutation (excl. `updateManyTenants` and `upsertTenants`).

```graphql
subscription {
    onUpdatedTenants {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Subscribing to a single Tenants upsert

Triggered from `upsertTenants` mutation.

```graphql
subscription {
    onUpsertedTenants {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Subscribing to a single Tenants deletion

Triggered from `deleteTenants` mutation (excl. `deleteManyTenants`).

```graphql
subscription {
    onDeletedTenants {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Subscribing to a single Tenants mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyTenants`).

```graphql
subscription {
    onMutatedTenants {
        id
        tenant_id
        email
        status
        subscription_type
    }
}
```

### Subscribing to many Tenants creations

Triggered from `createManyTenants` mutation.

```graphql
subscription {
    onCreatedManyTenants {
        count
    }
}
```

### Subscribing to many Tenants updates

Triggered from `updateManyTenants` mutation.

```graphql
subscription {
    onUpdatedManyTenants {
        count
    }
}
```

### Subscribing to many Tenants deletions

Triggered from `deleteManyTenants` mutation.

```graphql
subscription {
    onDeletedManyTenants {
        count
    }
}
```

### Subscribing to many Tenants mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyTenants {
        count
    }
}
```
