# DevopsCostlyResourceAlarm

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsCostlyResourceAlarm` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| alarm_name               | String      | true    | _false_           |
| cost                     | String      | _false_ | _false_           |
| alarm_priority           | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsCostlyResourceAlarm`: Read a single DevopsCostlyResourceAlarm.
-   `listDevopsCostlyResourceAlarms`: Read multiple DevopsCostlyResourceAlarms.
-   `countDevopsCostlyResourceAlarms`: Count all DevopsCostlyResourceAlarms.

### Querying a single DevopsCostlyResourceAlarm

Single DevopsCostlyResourceAlarm queries take one input:

-   `where`: `DevopsCostlyResourceAlarmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsCostlyResourceAlarm(where: { id: 2 }) {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsCostlyResourceAlarms

Multiple DevopsCostlyResourceAlarms queries can take four inputs:

-   `where`: `DevopsCostlyResourceAlarmWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceAlarmOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsCostlyResourceAlarms {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listDevopsCostlyResourceAlarms(skip: 0, take: 25) {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listDevopsCostlyResourceAlarms(
        where: { cost: { equals: Decimal } }
    ) {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listDevopsCostlyResourceAlarms(
        where: { cost: { not: { equals: Decimal } } }
    ) {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listDevopsCostlyResourceAlarms(
        orderBy: [{ cost: DESC }, { alarm_priority: ASC }]
    ) {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsCostlyResourceAlarms

Counting DevopsCostlyResourceAlarms queries can take four inputs:

-   `where`: `DevopsCostlyResourceAlarmWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsCostlyResourceAlarmOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsCostlyResourceAlarms
}
```

> `countDevopsCostlyResourceAlarms` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsCostlyResourceAlarm`: Create a single DevopsCostlyResourceAlarm.
-   `updateDevopsCostlyResourceAlarm`: Update a single DevopsCostlyResourceAlarm.
-   `upsertDevopsCostlyResourceAlarm`: Update existing OR create single DevopsCostlyResourceAlarm.
-   `deleteDevopsCostlyResourceAlarm`: Delete a single DevopsCostlyResourceAlarm.
-   `createManyDevopsCostlyResourceAlarms`: Create multiple DevopsCostlyResourceAlarms.
-   `updateManyDevopsCostlyResourceAlarms`: Update multiple DevopsCostlyResourceAlarms.
-   `deleteManyDevopsCostlyResourceAlarms`: Delete multiple DevopsCostlyResourceAlarms.

### Creating a single DevopsCostlyResourceAlarm

Single DevopsCostlyResourceAlarm create mutations take one input:

-   `data`: `DevopsCostlyResourceAlarmCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsCostlyResourceAlarm(
        data: {
            alarm_name: "Foo"
            cost: Decimal
            alarm_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsCostlyResourceAlarm

Single DevopsCostlyResourceAlarm update mutations take two inputs:

-   `where`: `DevopsCostlyResourceAlarmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsCostlyResourceAlarmUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsCostlyResourceAlarm(
        where: { id: 2 }
        data: {
            alarm_name: "Foo"
            cost: Decimal
            alarm_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsCostlyResourceAlarm

Single DevopsCostlyResourceAlarm delete mutations take one input:

-   `where`: `DevopsCostlyResourceAlarmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsCostlyResourceAlarm(where: { id: 2 }) {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsCostlyResourceAlarms

Multiple DevopsCostlyResourceAlarms create mutations take one input:

-   `data`: `[DevopsCostlyResourceAlarmCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsCostlyResourceAlarms(
        data: [
            { cost: Decimal }
            { cost: Decimal }
            { cost: Decimal }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyDevopsCostlyResourceAlarms` returns an integer that represents the number of records that were created.

### Updating multiple DevopsCostlyResourceAlarms

Multiple DevopsCostlyResourceAlarms update mutations take two inputs:

-   `where`: `DevopsCostlyResourceAlarmWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsCostlyResourceAlarmUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsCostlyResourceAlarms(
        where: { cost: Decimal }
        data: { cost: Decimal }
    ) {
        count
    }
}
```

> `updateManyDevopsCostlyResourceAlarms` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsCostlyResourceAlarms

Multiple DevopsCostlyResourceAlarms delete mutations can take one input:

-   `where`: `DevopsCostlyResourceAlarmWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsCostlyResourceAlarms(
        where: { cost: Decimal }
    ) {
        count
    }
}
```

> `deleteManyDevopsCostlyResourceAlarms` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsCostlyResourceAlarm creation

Triggered from `createDevopsCostlyResourceAlarm` mutation (excl. `createManyDevopsCostlyResourceAlarms` and `upsertDevopsCostlyResourceAlarm`).

```graphql
subscription {
    onCreatedDevopsCostlyResourceAlarm {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceAlarm update

Triggered from `updateDevopsCostlyResourceAlarm` mutation (excl. `updateManyDevopsCostlyResourceAlarms` and `upsertDevopsCostlyResourceAlarm`).

```graphql
subscription {
    onUpdatedDevopsCostlyResourceAlarm {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceAlarm upsert

Triggered from `upsertDevopsCostlyResourceAlarm` mutation.

```graphql
subscription {
    onUpsertedDevopsCostlyResourceAlarm {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceAlarm deletion

Triggered from `deleteDevopsCostlyResourceAlarm` mutation (excl. `deleteManyDevopsCostlyResourceAlarms`).

```graphql
subscription {
    onDeletedDevopsCostlyResourceAlarm {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsCostlyResourceAlarm mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsCostlyResourceAlarms`).

```graphql
subscription {
    onMutatedDevopsCostlyResourceAlarm {
        id
        alarm_name
        cost
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsCostlyResourceAlarm creations

Triggered from `createManyDevopsCostlyResourceAlarms` mutation.

```graphql
subscription {
    onCreatedManyDevopsCostlyResourceAlarms {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceAlarm updates

Triggered from `updateManyDevopsCostlyResourceAlarms` mutation.

```graphql
subscription {
    onUpdatedManyDevopsCostlyResourceAlarms {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceAlarm deletions

Triggered from `deleteManyDevopsCostlyResourceAlarms` mutation.

```graphql
subscription {
    onDeletedManyDevopsCostlyResourceAlarms {
        count
    }
}
```

### Subscribing to many DevopsCostlyResourceAlarm mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsCostlyResourceAlarms {
        count
    }
}
```
