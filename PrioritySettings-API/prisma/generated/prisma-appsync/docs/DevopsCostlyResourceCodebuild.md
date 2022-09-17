# DevopsCostlyResourceCodebuild

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceCodebuild` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| project_name             | String      | true    | _false_           |
| failed_count             | Int         | _false_ | _false_           |
| build_priority           | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceCodebuild`: Read a single DevopsCostlyResourceCodebuild.
-   `listDevopsCostlyResourceCodebuilds`: Read multiple DevopsCostlyResourceCodebuilds.
-   `countDevopsCostlyResourceCodebuilds`: Count all DevopsCostlyResourceCodebuilds.

### Querying a single DevopsCostlyResourceCodebuild

Single DevopsCostlyResourceCodebuild queries take one input:

-   `where`: `DevopsCostlyResourceCodebuildWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceCodebuild(where: { id: 2 }) {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsCostlyResourceCodebuilds

Multiple DevopsCostlyResourceCodebuilds queries can take four inputs:

-   `where`: `DevopsCostlyResourceCodebuildWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceCodebuildOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceCodebuilds {
        id
        project_name
        failed_count
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
    listDevopsCostlyResourceCodebuilds(skip: 0, take: 25) {
        id
        project_name
        failed_count
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
    listDevopsCostlyResourceCodebuilds(
        where: { failed_count: { equals: 2 } }
    ) {
        id
        project_name
        failed_count
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
    listDevopsCostlyResourceCodebuilds(
        where: { failed_count: { not: { equals: 2 } } }
    ) {
        id
        project_name
        failed_count
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
    listDevopsCostlyResourceCodebuilds(
        orderBy: [
            { failed_count: DESC }
            { build_priority: ASC }
        ]
    ) {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsCostlyResourceCodebuilds

Counting DevopsCostlyResourceCodebuilds queries can take four inputs:

-   `where`: `DevopsCostlyResourceCodebuildWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceCodebuildOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceCodebuilds
}
```

> `countDevopsCostlyResourceCodebuilds` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceCodebuild`: Create a single DevopsCostlyResourceCodebuild.
-   `updateDevopsCostlyResourceCodebuild`: Update a single DevopsCostlyResourceCodebuild.
-   `upsertDevopsCostlyResourceCodebuild`: Update existing OR create single DevopsCostlyResourceCodebuild.
-   `deleteDevopsCostlyResourceCodebuild`: Delete a single DevopsCostlyResourceCodebuild.
-   `createManyDevopsCostlyResourceCodebuilds`: Create multiple DevopsCostlyResourceCodebuilds.
-   `updateManyDevopsCostlyResourceCodebuilds`: Update multiple DevopsCostlyResourceCodebuilds.
-   `deleteManyDevopsCostlyResourceCodebuilds`: Delete multiple DevopsCostlyResourceCodebuilds.

### Creating a single DevopsCostlyResourceCodebuild

Single DevopsCostlyResourceCodebuild create mutations take one input:

-   `data`: `DevopsCostlyResourceCodebuildCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceCodebuild(
        data: {
            project_name: "Foo"
            failed_count: 2
            build_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsCostlyResourceCodebuild

Single DevopsCostlyResourceCodebuild update mutations take two inputs:

-   `where`: `DevopsCostlyResourceCodebuildWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceCodebuildUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceCodebuild(
        where: { id: 2 }
        data: {
            project_name: "Foo"
            failed_count: 2
            build_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsCostlyResourceCodebuild

Single DevopsCostlyResourceCodebuild delete mutations take one input:

-   `where`: `DevopsCostlyResourceCodebuildWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceCodebuild(where: { id: 2 }) {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsCostlyResourceCodebuilds

Multiple DevopsCostlyResourceCodebuilds create mutations take one input:

-   `data`: `[DevopsCostlyResourceCodebuildCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceCodebuilds(
        data: [
            { failed_count: 2 }
            { failed_count: 2 }
            { failed_count: 2 }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsCostlyResourceCodebuilds` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceCodebuilds

Multiple DevopsCostlyResourceCodebuilds update mutations take two inputs:

-   `where`: `DevopsCostlyResourceCodebuildWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceCodebuildUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceCodebuilds(
        where: { failed_count: 2 }
        data: { failed_count: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceCodebuilds` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceCodebuilds

Multiple DevopsCostlyResourceCodebuilds delete mutations can take one input:

-   `where`: `DevopsCostlyResourceCodebuildWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceCodebuilds(
        where: { failed_count: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceCodebuilds` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceCodebuild creation

Triggered from `createDevopsCostlyResourceCodebuild` mutation (excl. `createManyDevopsCostlyResourceCodebuilds` and `upsertDevopsCostlyResourceCodebuild`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceCodebuild {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodebuild update

Triggered from `updateDevopsCostlyResourceCodebuild` mutation (excl. `updateManyDevopsCostlyResourceCodebuilds` and `upsertDevopsCostlyResourceCodebuild`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceCodebuild {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodebuild upsert

Triggered from `upsertDevopsCostlyResourceCodebuild` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceCodebuild {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodebuild deletion

Triggered from `deleteDevopsCostlyResourceCodebuild` mutation (excl. `deleteManyDevopsCostlyResourceCodebuilds`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceCodebuild {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceCodebuild mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceCodebuilds`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceCodebuild {
        id
        project_name
        failed_count
        build_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsCostlyResourceCodebuild creations

Triggered from `createManyDevopsCostlyResourceCodebuilds` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceCodebuilds {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodebuild updates

Triggered from `updateManyDevopsCostlyResourceCodebuilds` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceCodebuilds {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodebuild deletions

Triggered from `deleteManyDevopsCostlyResourceCodebuilds` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceCodebuilds {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceCodebuild mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceCodebuilds {
        count
    }
}
```
