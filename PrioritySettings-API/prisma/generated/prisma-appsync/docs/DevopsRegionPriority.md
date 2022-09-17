# DevopsRegionPriority

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsRegionPriority` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| region                   | String      | true    | _false_           |
| resource_count           | Int         | _false_ | _false_           |
| region_priority          | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsRegionPriority`: Read a single DevopsRegionPriority.
-   `listDevopsRegionPriorities`: Read multiple DevopsRegionPriorities.
-   `countDevopsRegionPriorities`: Count all DevopsRegionPriorities.

### Querying a single DevopsRegionPriority

Single DevopsRegionPriority queries take one input:

-   `where`: `DevopsRegionPriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsRegionPriority(where: { id: 2 }) {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsRegionPriorities

Multiple DevopsRegionPriorities queries can take four inputs:

-   `where`: `DevopsRegionPriorityWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsRegionPriorityOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsRegionPriorities {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsRegionPriorities(skip: 0, take: 25) {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsRegionPriorities(
        where: { resource_count: { equals: 2 } }
    ) {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsRegionPriorities(
        where: { resource_count: { not: { equals: 2 } } }
    ) {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsRegionPriorities(
        orderBy: [
            { resource_count: DESC }
            { region_priority: ASC }
        ]
    ) {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsRegionPriorities

Counting DevopsRegionPriorities queries can take four inputs:

-   `where`: `DevopsRegionPriorityWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsRegionPriorityOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsRegionPriorities
}
```

> `countDevopsRegionPriorities` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsRegionPriority`: Create a single DevopsRegionPriority.
-   `updateDevopsRegionPriority`: Update a single DevopsRegionPriority.
-   `upsertDevopsRegionPriority`: Update existing OR create single DevopsRegionPriority.
-   `deleteDevopsRegionPriority`: Delete a single DevopsRegionPriority.
-   `createManyDevopsRegionPriorities`: Create multiple DevopsRegionPriorities.
-   `updateManyDevopsRegionPriorities`: Update multiple DevopsRegionPriorities.
-   `deleteManyDevopsRegionPriorities`: Delete multiple DevopsRegionPriorities.

### Creating a single DevopsRegionPriority

Single DevopsRegionPriority create mutations take one input:

-   `data`: `DevopsRegionPriorityCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsRegionPriority(
        data: {
            region: "Foo"
            resource_count: 2
            region_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsRegionPriority

Single DevopsRegionPriority update mutations take two inputs:

-   `where`: `DevopsRegionPriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsRegionPriorityUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsRegionPriority(
        where: { id: 2 }
        data: {
            region: "Foo"
            resource_count: 2
            region_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsRegionPriority

Single DevopsRegionPriority delete mutations take one input:

-   `where`: `DevopsRegionPriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsRegionPriority(where: { id: 2 }) {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsRegionPriorities

Multiple DevopsRegionPriorities create mutations take one input:

-   `data`: `[DevopsRegionPriorityCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsRegionPriorities(
        data: [
            { resource_count: 2 }
            { resource_count: 2 }
            { resource_count: 2 }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsRegionPriorities` returns an integer that represents the number of records that were created.

### Updating multiple DevopsRegionPriorities

Multiple DevopsRegionPriorities update mutations take two inputs:

-   `where`: `DevopsRegionPriorityWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsRegionPriorityUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsRegionPriorities(
        where: { resource_count: 2 }
        data: { resource_count: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsRegionPriorities` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsRegionPriorities

Multiple DevopsRegionPriorities delete mutations can take one input:

-   `where`: `DevopsRegionPriorityWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsRegionPriorities(
        where: { resource_count: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsRegionPriorities` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsRegionPriority creation

Triggered from `createDevopsRegionPriority` mutation (excl. `createManyDevopsRegionPriorities` and `upsertDevopsRegionPriority`).

```graphql
subscription {
    onCreatedDevopsRegionPriority {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsRegionPriority update

Triggered from `updateDevopsRegionPriority` mutation (excl. `updateManyDevopsRegionPriorities` and `upsertDevopsRegionPriority`).

```graphql
subscription {
    onUpdatedDevopsRegionPriority {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsRegionPriority upsert

Triggered from `upsertDevopsRegionPriority` mutation.

```graphql
subscription {
    onUpsertedDevopsRegionPriority {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsRegionPriority deletion

Triggered from `deleteDevopsRegionPriority` mutation (excl. `deleteManyDevopsRegionPriorities`).

```graphql
subscription {
    onDeletedDevopsRegionPriority {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsRegionPriority mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsRegionPriorities`).

```graphql
subscription {
    onMutatedDevopsRegionPriority {
        id
        region
        resource_count
        region_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsRegionPriority creations

Triggered from `createManyDevopsRegionPriorities` mutation.

```graphql
subscription {
    onCreatedManyDevopsRegionPriorities {
        count
    }
}
```

### Subscribing to many DevopsRegionPriority updates

Triggered from `updateManyDevopsRegionPriorities` mutation.

```graphql
subscription {
    onUpdatedManyDevopsRegionPriorities {
        count
    }
}
```

### Subscribing to many DevopsRegionPriority deletions

Triggered from `deleteManyDevopsRegionPriorities` mutation.

```graphql
subscription {
    onDeletedManyDevopsRegionPriorities {
        count
    }
}
```

### Subscribing to many DevopsRegionPriority mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsRegionPriorities {
        count
    }
}
```
