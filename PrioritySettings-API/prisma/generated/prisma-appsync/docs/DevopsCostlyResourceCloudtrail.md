# DevopsCostlyResourceCloudtrail

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceCloudtrail` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| trail_name               | String      | true    | _false_           |
| trail_value              | Int         | _false_ | _false_           |
| trail_priority           | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceCloudtrail`: Read a single DevopsCostlyResourceCloudtrail.
-   `listDevopsCostlyResourceCloudtrails`: Read multiple DevopsCostlyResourceCloudtrails.
-   `countDevopsCostlyResourceCloudtrails`: Count all DevopsCostlyResourceCloudtrails.

### Querying a single DevopsCostlyResourceCloudtrail

Single DevopsCostlyResourceCloudtrail queries take one input:

-   `where`: `DevopsCostlyResourceCloudtrailWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceCloudtrail(where: { id: 2 }) {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsCostlyResourceCloudtrails

Multiple DevopsCostlyResourceCloudtrails queries can take four inputs:

-   `where`: `DevopsCostlyResourceCloudtrailWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceCloudtrailOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceCloudtrails {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsCostlyResourceCloudtrails(skip: 0, take: 25) {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsCostlyResourceCloudtrails(
        where: { trail_value: { equals: 2 } }
    ) {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsCostlyResourceCloudtrails(
        where: { trail_value: { not: { equals: 2 } } }
    ) {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsCostlyResourceCloudtrails(
        orderBy: [
            { trail_value: DESC }
            { trail_priority: ASC }
        ]
    ) {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsCostlyResourceCloudtrails

Counting DevopsCostlyResourceCloudtrails queries can take four inputs:

-   `where`: `DevopsCostlyResourceCloudtrailWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceCloudtrailOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceCloudtrails
}
```

> `countDevopsCostlyResourceCloudtrails` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceCloudtrail`: Create a single DevopsCostlyResourceCloudtrail.
-   `updateDevopsCostlyResourceCloudtrail`: Update a single DevopsCostlyResourceCloudtrail.
-   `upsertDevopsCostlyResourceCloudtrail`: Update existing OR create single DevopsCostlyResourceCloudtrail.
-   `deleteDevopsCostlyResourceCloudtrail`: Delete a single DevopsCostlyResourceCloudtrail.
-   `createManyDevopsCostlyResourceCloudtrails`: Create multiple DevopsCostlyResourceCloudtrails.
-   `updateManyDevopsCostlyResourceCloudtrails`: Update multiple DevopsCostlyResourceCloudtrails.
-   `deleteManyDevopsCostlyResourceCloudtrails`: Delete multiple DevopsCostlyResourceCloudtrails.

### Creating a single DevopsCostlyResourceCloudtrail

Single DevopsCostlyResourceCloudtrail create mutations take one input:

-   `data`: `DevopsCostlyResourceCloudtrailCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceCloudtrail(
        data: {
            trail_name: "Foo"
            trail_value: 2
            trail_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsCostlyResourceCloudtrail

Single DevopsCostlyResourceCloudtrail update mutations take two inputs:

-   `where`: `DevopsCostlyResourceCloudtrailWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceCloudtrailUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceCloudtrail(
        where: { id: 2 }
        data: {
            trail_name: "Foo"
            trail_value: 2
            trail_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsCostlyResourceCloudtrail

Single DevopsCostlyResourceCloudtrail delete mutations take one input:

-   `where`: `DevopsCostlyResourceCloudtrailWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceCloudtrail(where: { id: 2 }) {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsCostlyResourceCloudtrails

Multiple DevopsCostlyResourceCloudtrails create mutations take one input:

-   `data`: `[DevopsCostlyResourceCloudtrailCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceCloudtrails(
        data: [
            { trail_value: 2 }
            { trail_value: 2 }
            { trail_value: 2 }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsCostlyResourceCloudtrails` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceCloudtrails

Multiple DevopsCostlyResourceCloudtrails update mutations take two inputs:

-   `where`: `DevopsCostlyResourceCloudtrailWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceCloudtrailUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceCloudtrails(
        where: { trail_value: 2 }
        data: { trail_value: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceCloudtrails` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceCloudtrails

Multiple DevopsCostlyResourceCloudtrails delete mutations can take one input:

-   `where`: `DevopsCostlyResourceCloudtrailWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceCloudtrails(
        where: { trail_value: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceCloudtrails` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceCloudtrail creation

Triggered from `createDevopsCostlyResourceCloudtrail` mutation (excl. `createManyDevopsCostlyResourceCloudtrails` and `upsertDevopsCostlyResourceCloudtrail`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceCloudtrail {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCloudtrail update

Triggered from `updateDevopsCostlyResourceCloudtrail` mutation (excl. `updateManyDevopsCostlyResourceCloudtrails` and `upsertDevopsCostlyResourceCloudtrail`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceCloudtrail {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCloudtrail upsert

Triggered from `upsertDevopsCostlyResourceCloudtrail` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceCloudtrail {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCloudtrail deletion

Triggered from `deleteDevopsCostlyResourceCloudtrail` mutation (excl. `deleteManyDevopsCostlyResourceCloudtrails`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceCloudtrail {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCloudtrail mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceCloudtrails`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceCloudtrail {
        id
        trail_name
        trail_value
        trail_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsCostlyResourceCloudtrail creations

Triggered from `createManyDevopsCostlyResourceCloudtrails` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceCloudtrails {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCloudtrail updates

Triggered from `updateManyDevopsCostlyResourceCloudtrails` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceCloudtrails {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCloudtrail deletions

Triggered from `deleteManyDevopsCostlyResourceCloudtrails` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceCloudtrails {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCloudtrail mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceCloudtrails {
        count
    }
}
```
