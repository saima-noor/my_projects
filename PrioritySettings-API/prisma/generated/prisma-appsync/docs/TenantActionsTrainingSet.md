# TenantActionsTrainingSet

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `TenantActionsTrainingSet` type.

| Field         | Scalar Type | Unique  | Required (create) |
| ------------- | ----------- | ------- | ----------------- |
| action_id     | Int         | true    | true              |
| date          | AWSDateTime | _false_ | true              |
| current_label | String      | _false_ | _false_           |
| new_label     | String      | _false_ | _false_           |
| tenant_id     | String      | _false_ | true              |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getTenantActionsTrainingSet`: Read a single TenantActionsTrainingSet.
-   `listTenantActionsTrainingSets`: Read multiple TenantActionsTrainingSets.
-   `countTenantActionsTrainingSets`: Count all TenantActionsTrainingSets.

### Querying a single TenantActionsTrainingSet

Single TenantActionsTrainingSet queries take one input:

-   `where`: `TenantActionsTrainingSetWhereUniqueInput!` A required object type specifying a field with a unique constraint (like action_id).

**Standard query**

```graphql
query {
    getTenantActionsTrainingSet(where: { action_id: 2 }) {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Querying multiple TenantActionsTrainingSets

Multiple TenantActionsTrainingSets queries can take four inputs:

-   `where`: `TenantActionsTrainingSetWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[TenantActionsTrainingSetOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listTenantActionsTrainingSets {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listTenantActionsTrainingSets(skip: 0, take: 25) {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listTenantActionsTrainingSets(
        where: { date: { equals: "dd/mm/YYYY" } }
    ) {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listTenantActionsTrainingSets(
        where: { date: { not: { equals: "dd/mm/YYYY" } } }
    ) {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listTenantActionsTrainingSets(
        orderBy: [{ date: DESC }, { current_label: ASC }]
    ) {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Counting TenantActionsTrainingSets

Counting TenantActionsTrainingSets queries can take four inputs:

-   `where`: `TenantActionsTrainingSetWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[TenantActionsTrainingSetOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countTenantActionsTrainingSets
}
```

> `countTenantActionsTrainingSets` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createTenantActionsTrainingSet`: Create a single TenantActionsTrainingSet.
-   `updateTenantActionsTrainingSet`: Update a single TenantActionsTrainingSet.
-   `upsertTenantActionsTrainingSet`: Update existing OR create single TenantActionsTrainingSet.
-   `deleteTenantActionsTrainingSet`: Delete a single TenantActionsTrainingSet.
-   `createManyTenantActionsTrainingSets`: Create multiple TenantActionsTrainingSets.
-   `updateManyTenantActionsTrainingSets`: Update multiple TenantActionsTrainingSets.
-   `deleteManyTenantActionsTrainingSets`: Delete multiple TenantActionsTrainingSets.

### Creating a single TenantActionsTrainingSet

Single TenantActionsTrainingSet create mutations take one input:

-   `data`: `TenantActionsTrainingSetCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createTenantActionsTrainingSet(
        data: {
            action_id: 2
            date: "dd/mm/YYYY"
            current_label: "Foo"
            new_label: "Foo"
            tenant_id: "Foo"
        }
    ) {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Updating a single TenantActionsTrainingSet

Single TenantActionsTrainingSet update mutations take two inputs:

-   `where`: `TenantActionsTrainingSetWhereUniqueInput!` A required object type specifying a field with a unique constraint (like action_id).
-   `data`: `TenantActionsTrainingSetUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateTenantActionsTrainingSet(
        where: { action_id: 2 }
        data: {
            action_id: 2
            date: "dd/mm/YYYY"
            current_label: "Foo"
            new_label: "Foo"
            tenant_id: "Foo"
        }
    ) {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Deleting a single TenantActionsTrainingSet

Single TenantActionsTrainingSet delete mutations take one input:

-   `where`: `TenantActionsTrainingSetWhereUniqueInput!` A required object type specifying a field with a unique constraint (like action_id).

**Standard delete mutation**

```graphql
mutation {
    deleteTenantActionsTrainingSet(
        where: { action_id: 2 }
    ) {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Creating multiple TenantActionsTrainingSets

Multiple TenantActionsTrainingSets create mutations take one input:

-   `data`: `[TenantActionsTrainingSetCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyTenantActionsTrainingSets(
        data: [
            { date: "dd/mm/YYYY" }
            { date: "dd/mm/YYYY" }
            { date: "dd/mm/YYYY" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyTenantActionsTrainingSets` returns an integer that represents the number of records that were created.

### Updating multiple TenantActionsTrainingSets

Multiple TenantActionsTrainingSets update mutations take two inputs:

-   `where`: `TenantActionsTrainingSetWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `TenantActionsTrainingSetUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyTenantActionsTrainingSets(
        where: { date: "dd/mm/YYYY" }
        data: { date: "dd/mm/YYYY" }
    ) {
        count
    }
}
```

> `updateManyTenantActionsTrainingSets` returns an integer that represents the number of records that were updated.

### Deleting multiple TenantActionsTrainingSets

Multiple TenantActionsTrainingSets delete mutations can take one input:

-   `where`: `TenantActionsTrainingSetWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyTenantActionsTrainingSets(
        where: { date: "dd/mm/YYYY" }
    ) {
        count
    }
}
```

> `deleteManyTenantActionsTrainingSets` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single TenantActionsTrainingSet creation

Triggered from `createTenantActionsTrainingSet` mutation (excl. `createManyTenantActionsTrainingSets` and `upsertTenantActionsTrainingSet`).

```graphql
subscription {
    onCreatedTenantActionsTrainingSet {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Subscribing to a single TenantActionsTrainingSet update

Triggered from `updateTenantActionsTrainingSet` mutation (excl. `updateManyTenantActionsTrainingSets` and `upsertTenantActionsTrainingSet`).

```graphql
subscription {
    onUpdatedTenantActionsTrainingSet {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Subscribing to a single TenantActionsTrainingSet upsert

Triggered from `upsertTenantActionsTrainingSet` mutation.

```graphql
subscription {
    onUpsertedTenantActionsTrainingSet {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Subscribing to a single TenantActionsTrainingSet deletion

Triggered from `deleteTenantActionsTrainingSet` mutation (excl. `deleteManyTenantActionsTrainingSets`).

```graphql
subscription {
    onDeletedTenantActionsTrainingSet {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Subscribing to a single TenantActionsTrainingSet mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyTenantActionsTrainingSets`).

```graphql
subscription {
    onMutatedTenantActionsTrainingSet {
        action_id
        date
        current_label
        new_label
        tenant_id
    }
}
```

### Subscribing to many TenantActionsTrainingSet creations

Triggered from `createManyTenantActionsTrainingSets` mutation.

```graphql
subscription {
    onCreatedManyTenantActionsTrainingSets {
        count
    }
}
```

### Subscribing to many TenantActionsTrainingSet updates

Triggered from `updateManyTenantActionsTrainingSets` mutation.

```graphql
subscription {
    onUpdatedManyTenantActionsTrainingSets {
        count
    }
}
```

### Subscribing to many TenantActionsTrainingSet deletions

Triggered from `deleteManyTenantActionsTrainingSets` mutation.

```graphql
subscription {
    onDeletedManyTenantActionsTrainingSets {
        count
    }
}
```

### Subscribing to many TenantActionsTrainingSet mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyTenantActionsTrainingSets {
        count
    }
}
```
