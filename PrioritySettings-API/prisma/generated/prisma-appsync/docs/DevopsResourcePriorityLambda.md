# DevopsResourcePriorityLambda

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePriorityLambda` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| function_name            | String      | true    | _false_           |
| frequency                | Int         | _false_ | _false_           |
| function_priority        | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsResourcePriorityLambda`: Read a single DevopsResourcePriorityLambda.
-   `listDevopsResourcePriorityLambdas`: Read multiple DevopsResourcePriorityLambdas.
-   `countDevopsResourcePriorityLambdas`: Count all DevopsResourcePriorityLambdas.

### Querying a single DevopsResourcePriorityLambda

Single DevopsResourcePriorityLambda queries take one input:

-   `where`: `DevopsResourcePriorityLambdaWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePriorityLambda(where: { id: 2 }) {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsResourcePriorityLambdas

Multiple DevopsResourcePriorityLambdas queries can take four inputs:

-   `where`: `DevopsResourcePriorityLambdaWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityLambdaOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePriorityLambdas {
        id
        function_name
        frequency
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
    listDevopsResourcePriorityLambdas(skip: 0, take: 25) {
        id
        function_name
        frequency
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
    listDevopsResourcePriorityLambdas(
        where: { frequency: { equals: 2 } }
    ) {
        id
        function_name
        frequency
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
    listDevopsResourcePriorityLambdas(
        where: { frequency: { not: { equals: 2 } } }
    ) {
        id
        function_name
        frequency
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
    listDevopsResourcePriorityLambdas(
        orderBy: [
            { frequency: DESC }
            { function_priority: ASC }
        ]
    ) {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsResourcePriorityLambdas

Counting DevopsResourcePriorityLambdas queries can take four inputs:

-   `where`: `DevopsResourcePriorityLambdaWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityLambdaOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePriorityLambdas
}
```

> `countDevopsResourcePriorityLambdas` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePriorityLambda`: Create a single DevopsResourcePriorityLambda.
-   `updateDevopsResourcePriorityLambda`: Update a single DevopsResourcePriorityLambda.
-   `upsertDevopsResourcePriorityLambda`: Update existing OR create single DevopsResourcePriorityLambda.
-   `deleteDevopsResourcePriorityLambda`: Delete a single DevopsResourcePriorityLambda.
-   `createManyDevopsResourcePriorityLambdas`: Create multiple DevopsResourcePriorityLambdas.
-   `updateManyDevopsResourcePriorityLambdas`: Update multiple DevopsResourcePriorityLambdas.
-   `deleteManyDevopsResourcePriorityLambdas`: Delete multiple DevopsResourcePriorityLambdas.

### Creating a single DevopsResourcePriorityLambda

Single DevopsResourcePriorityLambda create mutations take one input:

-   `data`: `DevopsResourcePriorityLambdaCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePriorityLambda(
        data: {
            function_name: "Foo"
            frequency: 2
            function_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsResourcePriorityLambda

Single DevopsResourcePriorityLambda update mutations take two inputs:

-   `where`: `DevopsResourcePriorityLambdaWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePriorityLambdaUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePriorityLambda(
        where: { id: 2 }
        data: {
            function_name: "Foo"
            frequency: 2
            function_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsResourcePriorityLambda

Single DevopsResourcePriorityLambda delete mutations take one input:

-   `where`: `DevopsResourcePriorityLambdaWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePriorityLambda(where: { id: 2 }) {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsResourcePriorityLambdas

Multiple DevopsResourcePriorityLambdas create mutations take one input:

-   `data`: `[DevopsResourcePriorityLambdaCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePriorityLambdas(
        data: [
            { frequency: 2 }
            { frequency: 2 }
            { frequency: 2 }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsResourcePriorityLambdas` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePriorityLambdas

Multiple DevopsResourcePriorityLambdas update mutations take two inputs:

-   `where`: `DevopsResourcePriorityLambdaWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePriorityLambdaUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePriorityLambdas(
        where: { frequency: 2 }
        data: { frequency: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePriorityLambdas` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePriorityLambdas

Multiple DevopsResourcePriorityLambdas delete mutations can take one input:

-   `where`: `DevopsResourcePriorityLambdaWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePriorityLambdas(
        where: { frequency: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePriorityLambdas` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePriorityLambda creation

Triggered from `createDevopsResourcePriorityLambda` mutation (excl. `createManyDevopsResourcePriorityLambdas` and `upsertDevopsResourcePriorityLambda`).

```graphql
subscription {
    onCreatedDevopsResourcePriorityLambda {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityLambda update

Triggered from `updateDevopsResourcePriorityLambda` mutation (excl. `updateManyDevopsResourcePriorityLambdas` and `upsertDevopsResourcePriorityLambda`).

```graphql
subscription {
    onUpdatedDevopsResourcePriorityLambda {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityLambda upsert

Triggered from `upsertDevopsResourcePriorityLambda` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePriorityLambda {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityLambda deletion

Triggered from `deleteDevopsResourcePriorityLambda` mutation (excl. `deleteManyDevopsResourcePriorityLambdas`).

```graphql
subscription {
    onDeletedDevopsResourcePriorityLambda {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityLambda mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePriorityLambdas`).

```graphql
subscription {
    onMutatedDevopsResourcePriorityLambda {
        id
        function_name
        frequency
        function_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsResourcePriorityLambda creations

Triggered from `createManyDevopsResourcePriorityLambdas` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePriorityLambdas {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityLambda updates

Triggered from `updateManyDevopsResourcePriorityLambdas` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePriorityLambdas {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityLambda deletions

Triggered from `deleteManyDevopsResourcePriorityLambdas` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePriorityLambdas {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityLambda mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePriorityLambdas {
        count
    }
}
```
