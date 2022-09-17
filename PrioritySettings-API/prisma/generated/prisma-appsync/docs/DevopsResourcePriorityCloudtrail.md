# DevopsResourcePriorityCloudtrail

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePriorityCloudtrail` type.

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

-   `getDevopsResourcePriorityCloudtrail`: Read a single DevopsResourcePriorityCloudtrail.
-   `listDevopsResourcePriorityCloudtrails`: Read multiple DevopsResourcePriorityCloudtrails.
-   `countDevopsResourcePriorityCloudtrails`: Count all DevopsResourcePriorityCloudtrails.

### Querying a single DevopsResourcePriorityCloudtrail

Single DevopsResourcePriorityCloudtrail queries take one input:

-   `where`: `DevopsResourcePriorityCloudtrailWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePriorityCloudtrail(where: { id: 2 }) {
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

### Querying multiple DevopsResourcePriorityCloudtrails

Multiple DevopsResourcePriorityCloudtrails queries can take four inputs:

-   `where`: `DevopsResourcePriorityCloudtrailWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityCloudtrailOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePriorityCloudtrails {
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
    listDevopsResourcePriorityCloudtrails(
        skip: 0
        take: 25
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

**Standard query with basic where filter**

```graphql
query {
    listDevopsResourcePriorityCloudtrails(
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
    listDevopsResourcePriorityCloudtrails(
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
    listDevopsResourcePriorityCloudtrails(
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

### Counting DevopsResourcePriorityCloudtrails

Counting DevopsResourcePriorityCloudtrails queries can take four inputs:

-   `where`: `DevopsResourcePriorityCloudtrailWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityCloudtrailOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePriorityCloudtrails
}
```

> `countDevopsResourcePriorityCloudtrails` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePriorityCloudtrail`: Create a single DevopsResourcePriorityCloudtrail.
-   `updateDevopsResourcePriorityCloudtrail`: Update a single DevopsResourcePriorityCloudtrail.
-   `upsertDevopsResourcePriorityCloudtrail`: Update existing OR create single DevopsResourcePriorityCloudtrail.
-   `deleteDevopsResourcePriorityCloudtrail`: Delete a single DevopsResourcePriorityCloudtrail.
-   `createManyDevopsResourcePriorityCloudtrails`: Create multiple DevopsResourcePriorityCloudtrails.
-   `updateManyDevopsResourcePriorityCloudtrails`: Update multiple DevopsResourcePriorityCloudtrails.
-   `deleteManyDevopsResourcePriorityCloudtrails`: Delete multiple DevopsResourcePriorityCloudtrails.

### Creating a single DevopsResourcePriorityCloudtrail

Single DevopsResourcePriorityCloudtrail create mutations take one input:

-   `data`: `DevopsResourcePriorityCloudtrailCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePriorityCloudtrail(
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

### Updating a single DevopsResourcePriorityCloudtrail

Single DevopsResourcePriorityCloudtrail update mutations take two inputs:

-   `where`: `DevopsResourcePriorityCloudtrailWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePriorityCloudtrailUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePriorityCloudtrail(
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

### Deleting a single DevopsResourcePriorityCloudtrail

Single DevopsResourcePriorityCloudtrail delete mutations take one input:

-   `where`: `DevopsResourcePriorityCloudtrailWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePriorityCloudtrail(
        where: { id: 2 }
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

### Creating multiple DevopsResourcePriorityCloudtrails

Multiple DevopsResourcePriorityCloudtrails create mutations take one input:

-   `data`: `[DevopsResourcePriorityCloudtrailCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePriorityCloudtrails(
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

> `createManyDevopsResourcePriorityCloudtrails` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePriorityCloudtrails

Multiple DevopsResourcePriorityCloudtrails update mutations take two inputs:

-   `where`: `DevopsResourcePriorityCloudtrailWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePriorityCloudtrailUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePriorityCloudtrails(
        where: { trail_value: 2 }
        data: { trail_value: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePriorityCloudtrails` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePriorityCloudtrails

Multiple DevopsResourcePriorityCloudtrails delete mutations can take one input:

-   `where`: `DevopsResourcePriorityCloudtrailWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePriorityCloudtrails(
        where: { trail_value: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePriorityCloudtrails` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePriorityCloudtrail creation

Triggered from `createDevopsResourcePriorityCloudtrail` mutation (excl. `createManyDevopsResourcePriorityCloudtrails` and `upsertDevopsResourcePriorityCloudtrail`).

```graphql
subscription {
    onCreatedDevopsResourcePriorityCloudtrail {
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

### Subscribing to a single DevopsResourcePriorityCloudtrail update

Triggered from `updateDevopsResourcePriorityCloudtrail` mutation (excl. `updateManyDevopsResourcePriorityCloudtrails` and `upsertDevopsResourcePriorityCloudtrail`).

```graphql
subscription {
    onUpdatedDevopsResourcePriorityCloudtrail {
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

### Subscribing to a single DevopsResourcePriorityCloudtrail upsert

Triggered from `upsertDevopsResourcePriorityCloudtrail` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePriorityCloudtrail {
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

### Subscribing to a single DevopsResourcePriorityCloudtrail deletion

Triggered from `deleteDevopsResourcePriorityCloudtrail` mutation (excl. `deleteManyDevopsResourcePriorityCloudtrails`).

```graphql
subscription {
    onDeletedDevopsResourcePriorityCloudtrail {
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

### Subscribing to a single DevopsResourcePriorityCloudtrail mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePriorityCloudtrails`).

```graphql
subscription {
    onMutatedDevopsResourcePriorityCloudtrail {
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

### Subscribing to many DevopsResourcePriorityCloudtrail creations

Triggered from `createManyDevopsResourcePriorityCloudtrails` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePriorityCloudtrails {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCloudtrail updates

Triggered from `updateManyDevopsResourcePriorityCloudtrails` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePriorityCloudtrails {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCloudtrail deletions

Triggered from `deleteManyDevopsResourcePriorityCloudtrails` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePriorityCloudtrails {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCloudtrail mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePriorityCloudtrails {
        count
    }
}
```
