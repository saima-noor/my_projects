# DevopsResourcePriorityTags

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePriorityTags` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| key                      | String      | _false_ | _false_           |
| value                    | String      | _false_ | _false_           |
| count                    | Int         | _false_ | _false_           |
| tag_priority             | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsResourcePriorityTags`: Read a single DevopsResourcePriorityTags.
-   `listDevopsResourcePriorityTags`: Read multiple DevopsResourcePriorityTags.
-   `countDevopsResourcePriorityTags`: Count all DevopsResourcePriorityTags.

### Querying a single DevopsResourcePriorityTags

Single DevopsResourcePriorityTags queries take one input:

-   `where`: `DevopsResourcePriorityTagsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePriorityTags(where: { id: 2 }) {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsResourcePriorityTags

Multiple DevopsResourcePriorityTags queries can take four inputs:

-   `where`: `DevopsResourcePriorityTagsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityTagsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePriorityTags {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsResourcePriorityTags(skip: 0, take: 25) {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsResourcePriorityTags(
        where: { key: { equals: "Foo" } }
    ) {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsResourcePriorityTags(
        where: { key: { not: { equals: "Foo" } } }
    ) {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsResourcePriorityTags(
        orderBy: [{ key: DESC }, { value: ASC }]
    ) {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsResourcePriorityTags

Counting DevopsResourcePriorityTags queries can take four inputs:

-   `where`: `DevopsResourcePriorityTagsWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityTagsOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePriorityTags
}
```

> `countDevopsResourcePriorityTags` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePriorityTags`: Create a single DevopsResourcePriorityTags.
-   `updateDevopsResourcePriorityTags`: Update a single DevopsResourcePriorityTags.
-   `upsertDevopsResourcePriorityTags`: Update existing OR create single DevopsResourcePriorityTags.
-   `deleteDevopsResourcePriorityTags`: Delete a single DevopsResourcePriorityTags.
-   `createManyDevopsResourcePriorityTags`: Create multiple DevopsResourcePriorityTags.
-   `updateManyDevopsResourcePriorityTags`: Update multiple DevopsResourcePriorityTags.
-   `deleteManyDevopsResourcePriorityTags`: Delete multiple DevopsResourcePriorityTags.

### Creating a single DevopsResourcePriorityTags

Single DevopsResourcePriorityTags create mutations take one input:

-   `data`: `DevopsResourcePriorityTagsCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePriorityTags(
        data: {
            key: "Foo"
            value: "Foo"
            count: 2
            tag_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsResourcePriorityTags

Single DevopsResourcePriorityTags update mutations take two inputs:

-   `where`: `DevopsResourcePriorityTagsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePriorityTagsUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePriorityTags(
        where: { id: 2 }
        data: {
            key: "Foo"
            value: "Foo"
            count: 2
            tag_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsResourcePriorityTags

Single DevopsResourcePriorityTags delete mutations take one input:

-   `where`: `DevopsResourcePriorityTagsWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePriorityTags(where: { id: 2 }) {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsResourcePriorityTags

Multiple DevopsResourcePriorityTags create mutations take one input:

-   `data`: `[DevopsResourcePriorityTagsCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePriorityTags(
        data: [
            { key: "Foo" }
            { key: "Foo" }
            { key: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsResourcePriorityTags` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePriorityTags

Multiple DevopsResourcePriorityTags update mutations take two inputs:

-   `where`: `DevopsResourcePriorityTagsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePriorityTagsUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePriorityTags(
        where: { key: "Foo" }
        data: { key: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePriorityTags` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePriorityTags

Multiple DevopsResourcePriorityTags delete mutations can take one input:

-   `where`: `DevopsResourcePriorityTagsWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePriorityTags(
        where: { key: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePriorityTags` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePriorityTags creation

Triggered from `createDevopsResourcePriorityTags` mutation (excl. `createManyDevopsResourcePriorityTags` and `upsertDevopsResourcePriorityTags`).

```graphql
subscription {
    onCreatedDevopsResourcePriorityTags {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityTags update

Triggered from `updateDevopsResourcePriorityTags` mutation (excl. `updateManyDevopsResourcePriorityTags` and `upsertDevopsResourcePriorityTags`).

```graphql
subscription {
    onUpdatedDevopsResourcePriorityTags {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityTags upsert

Triggered from `upsertDevopsResourcePriorityTags` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePriorityTags {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityTags deletion

Triggered from `deleteDevopsResourcePriorityTags` mutation (excl. `deleteManyDevopsResourcePriorityTags`).

```graphql
subscription {
    onDeletedDevopsResourcePriorityTags {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityTags mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePriorityTags`).

```graphql
subscription {
    onMutatedDevopsResourcePriorityTags {
        id
        key
        value
        count
        tag_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsResourcePriorityTags creations

Triggered from `createManyDevopsResourcePriorityTags` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePriorityTags {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityTags updates

Triggered from `updateManyDevopsResourcePriorityTags` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePriorityTags {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityTags deletions

Triggered from `deleteManyDevopsResourcePriorityTags` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePriorityTags {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityTags mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePriorityTags {
        count
    }
}
```
