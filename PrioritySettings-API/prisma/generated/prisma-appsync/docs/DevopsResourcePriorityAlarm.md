# DevopsResourcePriorityAlarm

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `DevopsResourcePriorityAlarm` type.

| Field                    | Scalar Type | Unique  | Required (create) |
| ------------------------ | ----------- | ------- | ----------------- |
| id                       | Int         | true    | true              |
| alarm_name               | String      | true    | _false_           |
| priority_value           | Int         | _false_ | _false_           |
| alarm_priority           | Int         | _false_ | _false_           |
| dev_engineer_priority    | Int         | _false_ | _false_           |
| devops_engineer_priority | Int         | _false_ | _false_           |
| dev_lead_priority        | Int         | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getDevopsResourcePriorityAlarm`: Read a single DevopsResourcePriorityAlarm.
-   `listDevopsResourcePriorityAlarms`: Read multiple DevopsResourcePriorityAlarms.
-   `countDevopsResourcePriorityAlarms`: Count all DevopsResourcePriorityAlarms.

### Querying a single DevopsResourcePriorityAlarm

Single DevopsResourcePriorityAlarm queries take one input:

-   `where`: `DevopsResourcePriorityAlarmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getDevopsResourcePriorityAlarm(where: { id: 2 }) {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Querying multiple DevopsResourcePriorityAlarms

Multiple DevopsResourcePriorityAlarms queries can take four inputs:

-   `where`: `DevopsResourcePriorityAlarmWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityAlarmOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listDevopsResourcePriorityAlarms {
        id
        alarm_name
        priority_value
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
    listDevopsResourcePriorityAlarms(skip: 0, take: 25) {
        id
        alarm_name
        priority_value
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
    listDevopsResourcePriorityAlarms(
        where: { priority_value: { equals: 2 } }
    ) {
        id
        alarm_name
        priority_value
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
    listDevopsResourcePriorityAlarms(
        where: { priority_value: { not: { equals: 2 } } }
    ) {
        id
        alarm_name
        priority_value
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
    listDevopsResourcePriorityAlarms(
        orderBy: [
            { priority_value: DESC }
            { alarm_priority: ASC }
        ]
    ) {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Counting DevopsResourcePriorityAlarms

Counting DevopsResourcePriorityAlarms queries can take four inputs:

-   `where`: `DevopsResourcePriorityAlarmWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[DevopsResourcePriorityAlarmOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countDevopsResourcePriorityAlarms
}
```

> `countDevopsResourcePriorityAlarms` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createDevopsResourcePriorityAlarm`: Create a single DevopsResourcePriorityAlarm.
-   `updateDevopsResourcePriorityAlarm`: Update a single DevopsResourcePriorityAlarm.
-   `upsertDevopsResourcePriorityAlarm`: Update existing OR create single DevopsResourcePriorityAlarm.
-   `deleteDevopsResourcePriorityAlarm`: Delete a single DevopsResourcePriorityAlarm.
-   `createManyDevopsResourcePriorityAlarms`: Create multiple DevopsResourcePriorityAlarms.
-   `updateManyDevopsResourcePriorityAlarms`: Update multiple DevopsResourcePriorityAlarms.
-   `deleteManyDevopsResourcePriorityAlarms`: Delete multiple DevopsResourcePriorityAlarms.

### Creating a single DevopsResourcePriorityAlarm

Single DevopsResourcePriorityAlarm create mutations take one input:

-   `data`: `DevopsResourcePriorityAlarmCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createDevopsResourcePriorityAlarm(
        data: {
            alarm_name: "Foo"
            priority_value: 2
            alarm_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Updating a single DevopsResourcePriorityAlarm

Single DevopsResourcePriorityAlarm update mutations take two inputs:

-   `where`: `DevopsResourcePriorityAlarmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `DevopsResourcePriorityAlarmUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateDevopsResourcePriorityAlarm(
        where: { id: 2 }
        data: {
            alarm_name: "Foo"
            priority_value: 2
            alarm_priority: 2
            dev_engineer_priority: 2
            devops_engineer_priority: 2
            dev_lead_priority: 2
        }
    ) {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Deleting a single DevopsResourcePriorityAlarm

Single DevopsResourcePriorityAlarm delete mutations take one input:

-   `where`: `DevopsResourcePriorityAlarmWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteDevopsResourcePriorityAlarm(where: { id: 2 }) {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Creating multiple DevopsResourcePriorityAlarms

Multiple DevopsResourcePriorityAlarms create mutations take one input:

-   `data`: `[DevopsResourcePriorityAlarmCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyDevopsResourcePriorityAlarms(
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

> `createManyDevopsResourcePriorityAlarms` returns an integer that represents the number of records that were created.

### Updating multiple DevopsResourcePriorityAlarms

Multiple DevopsResourcePriorityAlarms update mutations take two inputs:

-   `where`: `DevopsResourcePriorityAlarmWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `DevopsResourcePriorityAlarmUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyDevopsResourcePriorityAlarms(
        where: { priority_value: 2 }
        data: { priority_value: 2 }
    ) {
        count
    }
}
```

> `updateManyDevopsResourcePriorityAlarms` returns an integer that represents the number of records that were updated.

### Deleting multiple DevopsResourcePriorityAlarms

Multiple DevopsResourcePriorityAlarms delete mutations can take one input:

-   `where`: `DevopsResourcePriorityAlarmWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyDevopsResourcePriorityAlarms(
        where: { priority_value: 2 }
    ) {
        count
    }
}
```

> `deleteManyDevopsResourcePriorityAlarms` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single DevopsResourcePriorityAlarm creation

Triggered from `createDevopsResourcePriorityAlarm` mutation (excl. `createManyDevopsResourcePriorityAlarms` and `upsertDevopsResourcePriorityAlarm`).

```graphql
subscription {
    onCreatedDevopsResourcePriorityAlarm {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityAlarm update

Triggered from `updateDevopsResourcePriorityAlarm` mutation (excl. `updateManyDevopsResourcePriorityAlarms` and `upsertDevopsResourcePriorityAlarm`).

```graphql
subscription {
    onUpdatedDevopsResourcePriorityAlarm {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityAlarm upsert

Triggered from `upsertDevopsResourcePriorityAlarm` mutation.

```graphql
subscription {
    onUpsertedDevopsResourcePriorityAlarm {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityAlarm deletion

Triggered from `deleteDevopsResourcePriorityAlarm` mutation (excl. `deleteManyDevopsResourcePriorityAlarms`).

```graphql
subscription {
    onDeletedDevopsResourcePriorityAlarm {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to a single DevopsResourcePriorityAlarm mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyDevopsResourcePriorityAlarms`).

```graphql
subscription {
    onMutatedDevopsResourcePriorityAlarm {
        id
        alarm_name
        priority_value
        alarm_priority
        dev_engineer_priority
        devops_engineer_priority
        dev_lead_priority
    }
}
```

### Subscribing to many DevopsResourcePriorityAlarm creations

Triggered from `createManyDevopsResourcePriorityAlarms` mutation.

```graphql
subscription {
    onCreatedManyDevopsResourcePriorityAlarms {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityAlarm updates

Triggered from `updateManyDevopsResourcePriorityAlarms` mutation.

```graphql
subscription {
    onUpdatedManyDevopsResourcePriorityAlarms {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityAlarm deletions

Triggered from `deleteManyDevopsResourcePriorityAlarms` mutation.

```graphql
subscription {
    onDeletedManyDevopsResourcePriorityAlarms {
        count
    }
}
```

### Subscribing to many DevopsResourcePriorityAlarm mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyDevopsResourcePriorityAlarms {
        count
    }
}
```
