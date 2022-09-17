# DevopsRulesTable

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsRulesTable` type.

| Field           | Scalar Type | Unique  | Required (create) |
| --------------- | ----------- | ------- | ----------------- |
| rule_id         | Int         | true    | true              |
| rule_source     | String      | _false_ | _false_           |
| rule            | String      | _false_ | _false_           |
| base_importance | Int         | _false_ | _false_           |
| base_urgency    | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsRulesTable`: Read a single DevopsRulesTable.
-   `listDevopsRulesTables`: Read multiple DevopsRulesTables.
-   `countDevopsRulesTables`: Count all DevopsRulesTables.

### Querying a single DevopsRulesTable

Single DevopsRulesTable queries take one input:

-   `where`: `DevopsRulesTableWhereUniqueInput!` A required object type specifying a field with a unique constraint (like rule_id).

**Standard query**

```graphql
query {
    getDevopsRulesTable(where: { rule_id: 2 }) {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Querying multiple DevopsRulesTables

Multiple DevopsRulesTables queries can take four inputs:

-   `where`: `DevopsRulesTableWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsRulesTableOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsRulesTables {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsRulesTables(skip: 0, take: 25) {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsRulesTables(
        where: { rule_source: { equals: "Foo" } }
    ) {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsRulesTables(
        where: { rule_source: { not: { equals: "Foo" } } }
    ) {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsRulesTables(
        orderBy: [{ rule_source: DESC }, { rule: ASC }]
    ) {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Counting DevopsRulesTables

Counting DevopsRulesTables queries can take four inputs:

-   `where`: `DevopsRulesTableWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsRulesTableOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsRulesTables
}
```

> `countDevopsRulesTables` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsRulesTable`: Create a single DevopsRulesTable.
-   `updateDevopsRulesTable`: Update a single DevopsRulesTable.
-   `upsertDevopsRulesTable`: Update existing OR create single DevopsRulesTable.
-   `deleteDevopsRulesTable`: Delete a single DevopsRulesTable.
-   `createManyDevopsRulesTables`: Create multiple DevopsRulesTables.
-   `updateManyDevopsRulesTables`: Update multiple DevopsRulesTables.
-   `deleteManyDevopsRulesTables`: Delete multiple DevopsRulesTables.

### Creating a single DevopsRulesTable

Single DevopsRulesTable create mutations take one input:

-   `data`: `DevopsRulesTableCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsRulesTable(
        data: {
            rule_id: 2
            rule_source: "Foo"
            rule: "Foo"
            base_importance: 2
            base_urgency: 2
        }
    ) {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Updating a single DevopsRulesTable

Single DevopsRulesTable update mutations take two inputs:

-   `where`: `DevopsRulesTableWhereUniqueInput!` A required object type specifying a field with a unique constraint (like rule_id).
-   `data`: `DevopsRulesTableUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsRulesTable(
        where: { rule_id: 2 }
        data: {
            rule_id: 2
            rule_source: "Foo"
            rule: "Foo"
            base_importance: 2
            base_urgency: 2
        }
    ) {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Deleting a single DevopsRulesTable

Single DevopsRulesTable delete mutations take one input:

-   `where`: `DevopsRulesTableWhereUniqueInput!` A required object type specifying a field with a unique constraint (like rule_id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsRulesTable(where: { rule_id: 2 }) {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Creating multiple DevopsRulesTables

Multiple DevopsRulesTables create mutations take one input:

-   `data`: `[DevopsRulesTableCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsRulesTables(
        data: [
            { rule_source: "Foo" }
            { rule_source: "Foo" }
            { rule_source: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsRulesTables` returns an integer that represents the number of records that were created.

### Updating multiple DevopsRulesTables

Multiple DevopsRulesTables update mutations take two inputs:

-   `where`: `DevopsRulesTableWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsRulesTableUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsRulesTables(
        where: { rule_source: "Foo" }
        data: { rule_source: "Foo" }
    ) {
        count
    }
}
```

> `updateManyDevopsRulesTables` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsRulesTables

Multiple DevopsRulesTables delete mutations can take one input:

-   `where`: `DevopsRulesTableWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsRulesTables(
        where: { rule_source: "Foo" }
    ) {
        count
    }
}
```

> `deleteManyDevopsRulesTables` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsRulesTable creation

Triggered from `createDevopsRulesTable` mutation (excl. `createManyDevopsRulesTables` and `upsertDevopsRulesTable`).

```graphql
subscription {
    onCreatedDevopsRulesTable {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Subscribing to a single DevopsRulesTable update

Triggered from `updateDevopsRulesTable` mutation (excl. `updateManyDevopsRulesTables` and `upsertDevopsRulesTable`).

```graphql
subscription {
    onUpdatedDevopsRulesTable {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Subscribing to a single DevopsRulesTable upsert

Triggered from `upsertDevopsRulesTable` mutation.

```graphql
subscription {
    onUpsertedDevopsRulesTable {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Subscribing to a single DevopsRulesTable deletion

Triggered from `deleteDevopsRulesTable` mutation (excl. `deleteManyDevopsRulesTables`).

```graphql
subscription {
    onDeletedDevopsRulesTable {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Subscribing to a single DevopsRulesTable mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsRulesTables`).

```graphql
subscription {
    onMutatedDevopsRulesTable {
        rule_id
        rule_source
        rule
        base_importance
        base_urgency
    }
}
```

### Subscribing to many DevopsRulesTable creations

Triggered from `createManyDevopsRulesTables` mutation.

```graphql
subscription {
    onCreatedManyDevopsRulesTables {
        count
    }
}
```

### Subscribing to many DevopsRulesTable updates

Triggered from `updateManyDevopsRulesTables` mutation.

```graphql
subscription {
    onUpdatedManyDevopsRulesTables {
        count
    }
}
```

### Subscribing to many DevopsRulesTable deletions

Triggered from `deleteManyDevopsRulesTables` mutation.

```graphql
subscription {
    onDeletedManyDevopsRulesTables {
        count
    }
}
```

### Subscribing to many DevopsRulesTable mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsRulesTables {
        count
    }
}
```
