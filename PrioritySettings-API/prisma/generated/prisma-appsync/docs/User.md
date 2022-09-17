# User

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `User` type.

| Field     | Scalar Type          | Unique  | Required (create) |
| --------- | -------------------- | ------- | ----------------- |
| id        | Int                  | true    | true              |
| createdAt | AWSDateTime          | _false_ | true              |
| email     | AWSEmail             | true    | true              |
| name      | String               | _false_ | _false_           |
| role      | Role                 | _false_ | true              |
| posts     | [[Post!]](./Post.md) | _false_ | _false_           |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getUser`: Read a single User.
-   `listUsers`: Read multiple Users.
-   `countUsers`: Count all Users.

### Querying a single User

Single User queries take one input:

-   `where`: `UserWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getUser(where: { id: 2 }) {
        id
        createdAt
        email
        name
        role

        posts # Relation to many
    }
}
```

### Querying multiple Users

Multiple Users queries can take four inputs:

-   `where`: `UserWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[UserOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listUsers {
        id
        createdAt
        email
        name
        role

        posts # Relation to many
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listUsers(skip: 0, take: 25) {
        id
        createdAt
        email
        name
        role

        posts # Relation to many
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listUsers(
        where: { createdAt: { equals: "dd/mm/YYYY" } }
    ) {
        id
        createdAt
        email
        name
        role

        posts # Relation to many
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listUsers(
        where: {
            createdAt: { not: { equals: "dd/mm/YYYY" } }
        }
    ) {
        id
        createdAt
        email
        name
        role

        posts # Relation to many
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listUsers(
        orderBy: [{ createdAt: DESC }, { name: ASC }]
    ) {
        id
        createdAt
        email
        name
        role

        posts # Relation to many
    }
}
```

### Counting Users

Counting Users queries can take four inputs:

-   `where`: `UserWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[UserOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countUsers
}
```

> `countUsers` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createUser`: Create a single User.
-   `updateUser`: Update a single User.
-   `upsertUser`: Update existing OR create single User.
-   `deleteUser`: Delete a single User.
-   `createManyUsers`: Create multiple Users.
-   `updateManyUsers`: Update multiple Users.
-   `deleteManyUsers`: Delete multiple Users.

### Creating a single User

Single User create mutations take one input:

-   `data`: `UserCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createUser(
        data: { email: "Foo", name: "Foo", role: Role }
    ) {
        id
        createdAt
        email
        name
        role
    }
}
```

**Advanced create mutation using relation queries**

<details><summary>List of all nested queries available</summary>
<p>

```graphql
posts: {
    create: [UserPostsCreateInput], # Relation to many
    connect: [UserPostsWhereUniqueInput], # Relation to many
    connectOrCreate: [UserPostsConnectOrCreateInput] # Relation to many
}
```

</p>
</details>

```graphql
mutation {
    createUser(
        data: {
            posts: {
                connectOrCreate: [
                    {
                        where: UserWhereUniqueInput
                        create: UserCreateInput
                    }
                ]
            }
        }
    ) {
        id
    }
}
```

### Updating a single User

Single User update mutations take two inputs:

-   `where`: `UserWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `UserUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updateUser(
        where: { id: 2 }
        data: { email: "Foo", name: "Foo", role: Role }
    ) {
        id
        createdAt
        email
        name
        role
    }
}
```

**Advanced update mutation using relation queries**

<details><summary>List of all nested queries available</summary>
<p>

```graphql
posts: {
    create: [UserPostsCreateInput], # Relation to many
    connect: [UserPostsWhereUniqueInput], # Relation to many
    connectOrCreate: [UserPostsConnectOrCreateInput], # Relation to many
    update: [UserPostsUpdateUniqueInput], # Relation to many
    upsert: [UserPostsUpsertUniqueInput], # Relation to many
    delete: [UserPostsDeleteUniqueInput], # Relation to many
    disconnect: [UserPostsWhereUniqueInput], # Relation to many
    set: [UserPostsWhereUniqueInput], # Relation to many
    updateMany: [UserPostsUpdateManyInput], # Relation to many
    deleteMany: [UserPostsDeleteManyInput], # Relation to many
}
```

</p>
</details>

```graphql
mutation {
    updateUser(
        data: {
            posts: {
                connectOrCreate: [
                    {
                        where: UserWhereUniqueInput
                        create: UserCreateInput
                    }
                ]
            }
        }
    ) {
        id
    }
}
```

### Deleting a single User

Single User delete mutations take one input:

-   `where`: `UserWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deleteUser(where: { id: 2 }) {
        id
        createdAt
        email
        name
        role
    }
}
```

### Creating multiple Users

Multiple Users create mutations take one input:

-   `data`: `[UserCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyUsers(
        data: [
            { createdAt: "dd/mm/YYYY" }
            { createdAt: "dd/mm/YYYY" }
            { createdAt: "dd/mm/YYYY" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyUsers` returns an integer that represents the number of records that were created.

### Updating multiple Users

Multiple Users update mutations take two inputs:

-   `where`: `UserWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `UserUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyUsers(
        where: { createdAt: "dd/mm/YYYY" }
        data: { createdAt: "dd/mm/YYYY" }
    ) {
        count
    }
}
```

> `updateManyUsers` returns an integer that represents the number of records that were updated.

### Deleting multiple Users

Multiple Users delete mutations can take one input:

-   `where`: `UserWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyUsers(where: { createdAt: "dd/mm/YYYY" }) {
        count
    }
}
```

> `deleteManyUsers` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single User creation

Triggered from `createUser` mutation (excl. `createManyUsers` and `upsertUser`).

```graphql
subscription {
    onCreatedUser {
        id
        createdAt
        email
        name
        role
    }
}
```

### Subscribing to a single User update

Triggered from `updateUser` mutation (excl. `updateManyUsers` and `upsertUser`).

```graphql
subscription {
    onUpdatedUser {
        id
        createdAt
        email
        name
        role
    }
}
```

### Subscribing to a single User upsert

Triggered from `upsertUser` mutation.

```graphql
subscription {
    onUpsertedUser {
        id
        createdAt
        email
        name
        role
    }
}
```

### Subscribing to a single User deletion

Triggered from `deleteUser` mutation (excl. `deleteManyUsers`).

```graphql
subscription {
    onDeletedUser {
        id
        createdAt
        email
        name
        role
    }
}
```

### Subscribing to a single User mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyUsers`).

```graphql
subscription {
    onMutatedUser {
        id
        createdAt
        email
        name
        role
    }
}
```

### Subscribing to many User creations

Triggered from `createManyUsers` mutation.

```graphql
subscription {
    onCreatedManyUsers {
        count
    }
}
```

### Subscribing to many User updates

Triggered from `updateManyUsers` mutation.

```graphql
subscription {
    onUpdatedManyUsers {
        count
    }
}
```

### Subscribing to many User deletions

Triggered from `deleteManyUsers` mutation.

```graphql
subscription {
    onDeletedManyUsers {
        count
    }
}
```

### Subscribing to many User mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyUsers {
        count
    }
}
```
