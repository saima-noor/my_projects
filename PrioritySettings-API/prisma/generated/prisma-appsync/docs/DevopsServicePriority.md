# DevopsServicePriority

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsServicePriority` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| resource_type            | String      | true    | _false_           |
| resource_taws            | String      | _false_ | _false_           |
| count                    | Int         | _false_ | _false_           |
| service_priority         | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsServicePriority`: Read a single DevopsServicePriority.
-   `listDevopsServicePriorities`: Read multiple DevopsServicePriorities.
-   `countDevopsServicePriorities`: Count all DevopsServicePriorities.

### Querying a single DevopsServicePriority

Single DevopsServicePriority queries take one input:

-   `where`: `DevopsServicePriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsServicePriority(where: { id: 2 }) {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsServicePriorities

Multiple DevopsServicePriorities queries can take four inputs:

-   `where`: `DevopsServicePriorityWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsServicePriorityOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsServicePriorities {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsServicePriorities(skip: 0, take: 25) {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsServicePriorities(
        where: { resource_taws: { equals: "Foo" } }
    ) {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsServicePriorities(
        where: { resource_taws: { not: { equals: "Foo" } } }
    ) {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsServicePriorities(
        orderBy: [{ resource_taws: DESC }, { count: ASC }]
    ) {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsServicePriorities

Counting DevopsServicePriorities queries can take four inputs:

-   `where`: `DevopsServicePriorityWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsServicePriorityOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsServicePriorities
}
```

> `countDevopsServicePriorities` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsServicePriority`: Create a single DevopsServicePriority.
-   `updateDevopsServicePriority`: Update a single DevopsServicePriority.
-   `upsertDevopsServicePriority`: Update existing OR create single DevopsServicePriority.
-   `deleteDevopsServicePriority`: Delete a single DevopsServicePriority.
-   `createManyDevopsServicePriorities`: Create multiple DevopsServicePriorities.
-   `updateManyDevopsServicePriorities`: Update multiple DevopsServicePriorities.
-   `deleteManyDevopsServicePriorities`: Delete multiple DevopsServicePriorities.

### Creating a single DevopsServicePriority

Single DevopsServicePriority create mutations take one input:

-   `data`: `DevopsServicePriorityCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsServicePriority(
        data: {
            resource_type: "Foo"
            resource_taws: "Foo"
            count: 2
            service_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsServicePriority

Single DevopsServicePriority update mutations take two inputs:

-   `where`: `DevopsServicePriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsServicePriorityUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsServicePriority(
        where: { id: 2 }
        data: {
            resource_type: "Foo"
            resource_taws: "Foo"
            count: 2
            service_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsServicePriority

Single DevopsServicePriority delete mutations take one input:

-   `where`: `DevopsServicePriorityWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsServicePriority(where: { id: 2 }) {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsServicePriorities

Multiple DevopsServicePriorities create mutations take one input:

-   `data`: `[DevopsServicePriorityCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsServicePriorities(
        data: [
            { resource_taws: "Foo" }
            { resource_taws: "Foo" }
            { resource_taws: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsServicePriorities` returns an integer that represents the number of records that were created.

### Updating multiple DevopsServicePriorities

Multiple DevopsServicePriorities update mutations take two inputs:

-   `where`: `DevopsServicePriorityWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsServicePriorityUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsServicePriorities(
        where: { resource_taws: "Foo" }
        data: { resource_taws: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsServicePriorities` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsServicePriorities

Multiple DevopsServicePriorities delete mutations can take one input:

-   `where`: `DevopsServicePriorityWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsServicePriorities(
        where: { resource_taws: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsServicePriorities` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsServicePriority creation

Triggered from `createDevopsServicePriority` mutation (excl. `createManyDevopsServicePriorities` and `upsertDevopsServicePriority`).

```graphql
subscription {
    onCreatedDevopsServicePriority {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsServicePriority update

Triggered from `updateDevopsServicePriority` mutation (excl. `updateManyDevopsServicePriorities` and `upsertDevopsServicePriority`).

```graphql
subscription {
    onUpdatedDevopsServicePriority {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsServicePriority upsert

Triggered from `upsertDevopsServicePriority` mutation.

```graphql
subscription {
    onUpsertedDevopsServicePriority {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsServicePriority deletion

Triggered from `deleteDevopsServicePriority` mutation (excl. `deleteManyDevopsServicePriorities`).

```graphql
subscription {
    onDeletedDevopsServicePriority {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsServicePriority mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsServicePriorities`).

```graphql
subscription {
    onMutatedDevopsServicePriority {
        id
        resource_type
        resource_taws
        count
        service_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsServicePriority creations

Triggered from `createManyDevopsServicePriorities` mutation.

```graphql
subscription {
    onCreatedManyDevopsServicePriorities {
        count
    }
}
```

### Subscribing to many DevopsServicePriority updates

Triggered from `updateManyDevopsServicePriorities` mutation.

```graphql
subscription {
    onUpdatedManyDevopsServicePriorities {
        count
    }
}
```

### Subscribing to many DevopsServicePriority deletions

Triggered from `deleteManyDevopsServicePriorities` mutation.

```graphql
subscription {
    onDeletedManyDevopsServicePriorities {
        count
    }
}
```

### Subscribing to many DevopsServicePriority mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsServicePriorities {
        count
    }
}
```
