# DevopsResourcePriorityCodebuild

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePriorityCodebuild` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| project_name             | String      | true    | _false_           |
| succeed_count            | Int         | _false_ | _false_           |
| build_priority           | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsResourcePriorityCodebuild`: Read a single DevopsResourcePriorityCodebuild.
-   `listDevopsResourcePriorityCodebuilds`: Read multiple DevopsResourcePriorityCodebuilds.
-   `countDevopsResourcePriorityCodebuilds`: Count all DevopsResourcePriorityCodebuilds.

### Querying a single DevopsResourcePriorityCodebuild

Single DevopsResourcePriorityCodebuild queries take one input:

-   `where`: `DevopsResourcePriorityCodebuildWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePriorityCodebuild(where: { id: 2 }) {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsResourcePriorityCodebuilds

Multiple DevopsResourcePriorityCodebuilds queries can take four inputs:

-   `where`: `DevopsResourcePriorityCodebuildWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityCodebuildOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePriorityCodebuilds {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsResourcePriorityCodebuilds(
        skip: 0
        take: 25
    ) {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsResourcePriorityCodebuilds(
        where: { succeed_count: { equals: 2 } }
    ) {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsResourcePriorityCodebuilds(
        where: { succeed_count: { not: { equals: 2 } } }
    ) {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsResourcePriorityCodebuilds(
        orderBy: [
            { succeed_count: DESC }
            { build_priority: ASC }
        ]
    ) {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsResourcePriorityCodebuilds

Counting DevopsResourcePriorityCodebuilds queries can take four inputs:

-   `where`: `DevopsResourcePriorityCodebuildWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityCodebuildOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePriorityCodebuilds
}
```

> `countDevopsResourcePriorityCodebuilds` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePriorityCodebuild`: Create a single DevopsResourcePriorityCodebuild.
-   `updateDevopsResourcePriorityCodebuild`: Update a single DevopsResourcePriorityCodebuild.
-   `upsertDevopsResourcePriorityCodebuild`: Update existing OR create single DevopsResourcePriorityCodebuild.
-   `deleteDevopsResourcePriorityCodebuild`: Delete a single DevopsResourcePriorityCodebuild.
-   `createManyDevopsResourcePriorityCodebuilds`: Create multiple DevopsResourcePriorityCodebuilds.
-   `updateManyDevopsResourcePriorityCodebuilds`: Update multiple DevopsResourcePriorityCodebuilds.
-   `deleteManyDevopsResourcePriorityCodebuilds`: Delete multiple DevopsResourcePriorityCodebuilds.

### Creating a single DevopsResourcePriorityCodebuild

Single DevopsResourcePriorityCodebuild create mutations take one input:

-   `data`: `DevopsResourcePriorityCodebuildCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePriorityCodebuild(
        data: {
            project_name: "Foo"
            succeed_count: 2
            build_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsResourcePriorityCodebuild

Single DevopsResourcePriorityCodebuild update mutations take two inputs:

-   `where`: `DevopsResourcePriorityCodebuildWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePriorityCodebuildUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePriorityCodebuild(
        where: { id: 2 }
        data: {
            project_name: "Foo"
            succeed_count: 2
            build_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsResourcePriorityCodebuild

Single DevopsResourcePriorityCodebuild delete mutations take one input:

-   `where`: `DevopsResourcePriorityCodebuildWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePriorityCodebuild(
        where: { id: 2 }
    ) {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsResourcePriorityCodebuilds

Multiple DevopsResourcePriorityCodebuilds create mutations take one input:

-   `data`: `[DevopsResourcePriorityCodebuildCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePriorityCodebuilds(
        data: [
            { succeed_count: 2 }
            { succeed_count: 2 }
            { succeed_count: 2 }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsResourcePriorityCodebuilds` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePriorityCodebuilds

Multiple DevopsResourcePriorityCodebuilds update mutations take two inputs:

-   `where`: `DevopsResourcePriorityCodebuildWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePriorityCodebuildUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePriorityCodebuilds(
        where: { succeed_count: 2 }
        data: { succeed_count: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePriorityCodebuilds` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePriorityCodebuilds

Multiple DevopsResourcePriorityCodebuilds delete mutations can take one input:

-   `where`: `DevopsResourcePriorityCodebuildWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePriorityCodebuilds(
        where: { succeed_count: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePriorityCodebuilds` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePriorityCodebuild creation

Triggered from `createDevopsResourcePriorityCodebuild` mutation (excl. `createManyDevopsResourcePriorityCodebuilds` and `upsertDevopsResourcePriorityCodebuild`).

```graphql
subscription {
    onCreatedDevopsResourcePriorityCodebuild {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityCodebuild update

Triggered from `updateDevopsResourcePriorityCodebuild` mutation (excl. `updateManyDevopsResourcePriorityCodebuilds` and `upsertDevopsResourcePriorityCodebuild`).

```graphql
subscription {
    onUpdatedDevopsResourcePriorityCodebuild {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityCodebuild upsert

Triggered from `upsertDevopsResourcePriorityCodebuild` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePriorityCodebuild {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityCodebuild deletion

Triggered from `deleteDevopsResourcePriorityCodebuild` mutation (excl. `deleteManyDevopsResourcePriorityCodebuilds`).

```graphql
subscription {
    onDeletedDevopsResourcePriorityCodebuild {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityCodebuild mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePriorityCodebuilds`).

```graphql
subscription {
    onMutatedDevopsResourcePriorityCodebuild {
        id
        project_name
        succeed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsResourcePriorityCodebuild creations

Triggered from `createManyDevopsResourcePriorityCodebuilds` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePriorityCodebuilds {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCodebuild updates

Triggered from `updateManyDevopsResourcePriorityCodebuilds` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePriorityCodebuilds {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCodebuild deletions

Triggered from `deleteManyDevopsResourcePriorityCodebuilds` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePriorityCodebuilds {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityCodebuild mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePriorityCodebuilds {
        count
    }
}
```
