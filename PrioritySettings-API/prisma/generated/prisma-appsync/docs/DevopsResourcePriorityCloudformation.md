# DevopsResourcePriorityCloudformation

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePriorityCloudformation` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| stack_name               | String      | true    | _false_           |
| priority_value           | Int         | _false_ | _false_           |
| stack_priority           | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsResourcePriorityCloudformation`: Read a single DevopsResourcePriorityCloudformation.
-   `listDevopsResourcePriorityCloudformations`: Read multiple DevopsResourcePriorityCloudformations.
-   `countDevopsResourcePriorityCloudformations`: Count all DevopsResourcePriorityCloudformations.

### Querying a single DevopsResourcePriorityCloudformation

Single DevopsResourcePriorityCloudformation queries take one input:

-   `where`: `DevopsResourcePriorityCloudformationWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePriorityCloudformation(
        where: { id: 2 }
    ) {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsResourcePriorityCloudformations

Multiple DevopsResourcePriorityCloudformations queries can take four inputs:

-   `where`: `DevopsResourcePriorityCloudformationWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityCloudformationOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePriorityCloudformations {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsResourcePriorityCloudformations(
        skip: 0
        take: 25
    ) {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsResourcePriorityCloudformations(
        where: { priority_value: { equals: 2 } }
    ) {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsResourcePriorityCloudformations(
        where: { priority_value: { not: { equals: 2 } } }
    ) {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsResourcePriorityCloudformations(
        orderBy: [
            { priority_value: DESC }
            { stack_priority: ASC }
        ]
    ) {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsResourcePriorityCloudformations

Counting DevopsResourcePriorityCloudformations queries can take four inputs:

-   `where`: `DevopsResourcePriorityCloudformationWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityCloudformationOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePriorityCloudformations
}
```

> `countDevopsResourcePriorityCloudformations` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePriorityCloudformation`: Create a single DevopsResourcePriorityCloudformation.
-   `updateDevopsResourcePriorityCloudformation`: Update a single DevopsResourcePriorityCloudformation.
-   `upsertDevopsResourcePriorityCloudformation`: Update existing OR create single DevopsResourcePriorityCloudformation.
-   `deleteDevopsResourcePriorityCloudformation`: Delete a single DevopsResourcePriorityCloudformation.
-   `createManyDevopsResourcePriorityCloudformations`: Create multiple DevopsResourcePriorityCloudformations.
-   `updateManyDevopsResourcePriorityCloudformations`: Update multiple DevopsResourcePriorityCloudformations.
-   `deleteManyDevopsResourcePriorityCloudformations`: Delete multiple DevopsResourcePriorityCloudformations.

### Creating a single DevopsResourcePriorityCloudformation

Single DevopsResourcePriorityCloudformation create mutations take one input:

-   `data`: `DevopsResourcePriorityCloudformationCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePriorityCloudformation(
        data: {
            stack_name: "Foo"
            priority_value: 2
            stack_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsResourcePriorityCloudformation

Single DevopsResourcePriorityCloudformation update mutations take two inputs:

-   `where`: `DevopsResourcePriorityCloudformationWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePriorityCloudformationUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePriorityCloudformation(
        where: { id: 2 }
        data: {
            stack_name: "Foo"
            priority_value: 2
            stack_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsResourcePriorityCloudformation

Single DevopsResourcePriorityCloudformation delete mutations take one input:

-   `where`: `DevopsResourcePriorityCloudformationWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePriorityCloudformation(
        where: { id: 2 }
    ) {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsResourcePriorityCloudformations

Multiple DevopsResourcePriorityCloudformations create mutations take one input:

-   `data`: `[DevopsResourcePriorityCloudformationCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePriorityCloudformations(
        data: [
            { priority_value: 2 }
            { priority_value: 2 }
            { priority_value: 2 }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsResourcePriorityCloudformations` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePriorityCloudformations

Multiple DevopsResourcePriorityCloudformations update mutations take two inputs:

-   `where`: `DevopsResourcePriorityCloudformationWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePriorityCloudformationUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePriorityCloudformations(
        where: { priority_value: 2 }
        data: { priority_value: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePriorityCloudformations` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePriorityCloudformations

Multiple DevopsResourcePriorityCloudformations delete mutations can take one input:

-   `where`: `DevopsResourcePriorityCloudformationWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePriorityCloudformations(
        where: { priority_value: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePriorityCloudformations` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePriorityCloudformation creation

Triggered from `createDevopsResourcePriorityCloudformation` mutation (excl. `createManyDevopsResourcePriorityCloudformations` and `upsertDevopsResourcePriorityCloudformation`).

```graphql
subscription {
    onCreatedDevopsResourcePriorityCloudformation {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityCloudformation update

Triggered from `updateDevopsResourcePriorityCloudformation` mutation (excl. `updateManyDevopsResourcePriorityCloudformations` and `upsertDevopsResourcePriorityCloudformation`).

```graphql
subscription {
    onUpdatedDevopsResourcePriorityCloudformation {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityCloudformation upsert

Triggered from `upsertDevopsResourcePriorityCloudformation` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePriorityCloudformation {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityCloudformation deletion

Triggered from `deleteDevopsResourcePriorityCloudformation` mutation (excl. `deleteManyDevopsResourcePriorityCloudformations`).

```graphql
subscription {
    onDeletedDevopsResourcePriorityCloudformation {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityCloudformation mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePriorityCloudformations`).

```graphql
subscription {
    onMutatedDevopsResourcePriorityCloudformation {
        id
        stack_name
        priority_value
        stack_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsResourcePriorityCloudformation creations

Triggered from `createManyDevopsResourcePriorityCloudformations` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePriorityCloudformations {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCloudformation updates

Triggered from `updateManyDevopsResourcePriorityCloudformations` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePriorityCloudformations {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCloudformation deletions

Triggered from `deleteManyDevopsResourcePriorityCloudformations` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePriorityCloudformations {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCloudformation mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePriorityCloudformations {
        count
    }
}
```
