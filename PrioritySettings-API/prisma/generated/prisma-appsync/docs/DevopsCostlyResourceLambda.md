# DevopsCostlyResourceLambda

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceLambda` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| function_name            | String      | true    | _false_           |
| error_count              | Int         | _false_ | _false_           |
| function_priority        | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceLambda`: Read a single DevopsCostlyResourceLambda.
-   `listDevopsCostlyResourceLambdas`: Read multiple DevopsCostlyResourceLambdas.
-   `countDevopsCostlyResourceLambdas`: Count all DevopsCostlyResourceLambdas.

### Querying a single DevopsCostlyResourceLambda

Single DevopsCostlyResourceLambda queries take one input:

-   `where`: `DevopsCostlyResourceLambdaWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceLambda(where: { id: 2 }) {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsCostlyResourceLambdas

Multiple DevopsCostlyResourceLambdas queries can take four inputs:

-   `where`: `DevopsCostlyResourceLambdaWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceLambdaOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceLambdas {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsCostlyResourceLambdas(skip: 0, take: 25) {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsCostlyResourceLambdas(
        where: { error_count: { equals: 2 } }
    ) {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsCostlyResourceLambdas(
        where: { error_count: { not: { equals: 2 } } }
    ) {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsCostlyResourceLambdas(
        orderBy: [
            { error_count: DESC }
            { function_priority: ASC }
        ]
    ) {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsCostlyResourceLambdas

Counting DevopsCostlyResourceLambdas queries can take four inputs:

-   `where`: `DevopsCostlyResourceLambdaWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceLambdaOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceLambdas
}
```

> `countDevopsCostlyResourceLambdas` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceLambda`: Create a single DevopsCostlyResourceLambda.
-   `updateDevopsCostlyResourceLambda`: Update a single DevopsCostlyResourceLambda.
-   `upsertDevopsCostlyResourceLambda`: Update existing OR create single DevopsCostlyResourceLambda.
-   `deleteDevopsCostlyResourceLambda`: Delete a single DevopsCostlyResourceLambda.
-   `createManyDevopsCostlyResourceLambdas`: Create multiple DevopsCostlyResourceLambdas.
-   `updateManyDevopsCostlyResourceLambdas`: Update multiple DevopsCostlyResourceLambdas.
-   `deleteManyDevopsCostlyResourceLambdas`: Delete multiple DevopsCostlyResourceLambdas.

### Creating a single DevopsCostlyResourceLambda

Single DevopsCostlyResourceLambda create mutations take one input:

-   `data`: `DevopsCostlyResourceLambdaCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceLambda(
        data: {
            function_name: "Foo"
            error_count: 2
            function_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsCostlyResourceLambda

Single DevopsCostlyResourceLambda update mutations take two inputs:

-   `where`: `DevopsCostlyResourceLambdaWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceLambdaUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceLambda(
        where: { id: 2 }
        data: {
            function_name: "Foo"
            error_count: 2
            function_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsCostlyResourceLambda

Single DevopsCostlyResourceLambda delete mutations take one input:

-   `where`: `DevopsCostlyResourceLambdaWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceLambda(where: { id: 2 }) {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsCostlyResourceLambdas

Multiple DevopsCostlyResourceLambdas create mutations take one input:

-   `data`: `[DevopsCostlyResourceLambdaCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceLambdas(
        data: [
            { error_count: 2 }
            { error_count: 2 }
            { error_count: 2 }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsCostlyResourceLambdas` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceLambdas

Multiple DevopsCostlyResourceLambdas update mutations take two inputs:

-   `where`: `DevopsCostlyResourceLambdaWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceLambdaUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceLambdas(
        where: { error_count: 2 }
        data: { error_count: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceLambdas` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceLambdas

Multiple DevopsCostlyResourceLambdas delete mutations can take one input:

-   `where`: `DevopsCostlyResourceLambdaWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceLambdas(
        where: { error_count: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceLambdas` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceLambda creation

Triggered from `createDevopsCostlyResourceLambda` mutation (excl. `createManyDevopsCostlyResourceLambdas` and `upsertDevopsCostlyResourceLambda`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceLambda {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceLambda update

Triggered from `updateDevopsCostlyResourceLambda` mutation (excl. `updateManyDevopsCostlyResourceLambdas` and `upsertDevopsCostlyResourceLambda`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceLambda {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceLambda upsert

Triggered from `upsertDevopsCostlyResourceLambda` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceLambda {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceLambda deletion

Triggered from `deleteDevopsCostlyResourceLambda` mutation (excl. `deleteManyDevopsCostlyResourceLambdas`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceLambda {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceLambda mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceLambdas`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceLambda {
        id
        function_name
        error_count
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsCostlyResourceLambda creations

Triggered from `createManyDevopsCostlyResourceLambdas` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceLambdas {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceLambda updates

Triggered from `updateManyDevopsCostlyResourceLambdas` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceLambdas {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceLambda deletions

Triggered from `deleteManyDevopsCostlyResourceLambdas` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceLambdas {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceLambda mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceLambdas {
        count
    }
}
```
