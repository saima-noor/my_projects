# Post

-   [Fields](#fields)
-   [Queries](#queries)
-   [Mutations](#mutations)
-   [Subscriptions](#subscriptions)

## Fields

List of fields available in the `Post` type.

| Field     | Scalar Type       | Unique  | Required (create) |
| --------- | ----------------- | ------- | ----------------- |
| id        | Int               | true    | true              |
| author    | [User](./User.md) | _false_ | _false_           |
| authorId  | Int               | true    | _false_           |
| title     | String            | _false_ | true              |
| views     | Int               | _false_ | _false_           |
| published | Boolean           | _false_ | _false_           |
| createdAt | AWSDateTime       | _false_ | true              |
| updatedAt | AWSDateTime       | _false_ | true              |

## Queries

Queries are responsible for all `Read` operations.

The generated queries are:

-   `getPost`: Read a single Post.
-   `listPosts`: Read multiple Posts.
-   `countPosts`: Count all Posts.

### Querying a single Post

Single Post queries take one input:

-   `where`: `PostWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard query**

```graphql
query {
    getPost(where: { id: 2 }) {
        id
        author # Relation to one
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

### Querying multiple Posts

Multiple Posts queries can take four inputs:

-   `where`: `PostWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[PostOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    listPosts {
        id
        author # Relation to one
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

**Standard query with offset pagination**

```graphql
query {
    listPosts(skip: 0, take: 25) {
        id
        author # Relation to one
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

**Standard query with basic where filter**

```graphql
query {
    listPosts(where: { title: { equals: "Foo" } }) {
        id
        author # Relation to one
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

**Standard query with more advanced where filter**

```graphql
query {
    listPosts(
        where: { title: { not: { equals: "Foo" } } }
    ) {
        id
        author # Relation to one
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

**Standard query with orderBy**

```graphql
query {
    listPosts(orderBy: [{ title: DESC }, { views: ASC }]) {
        id
        author # Relation to one
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

### Counting Posts

Counting Posts queries can take four inputs:

-   `where`: `PostWhereFilterInput` An optional object type to filter the content based on a nested set of criteria.
-   `orderBy`: `[PostOrderByInput]` An optional array to select which field(s) and order to sort the records on. Sorting can be in ascending order `ASC` or descending order `DESC`.
-   `skip`: `Int` An optional number that specifies how many of the returned objects in the list should be skipped.
-   `take`: `Int` An optional number that specifies how many objects should be returned in the list.

**Standard query**

```graphql
query {
    countPosts
}
```

> `countPosts` returns an integer that represents the number of records found.

## Mutations

Mutations are responsible for all `Create`, `Update`, and `Delete` operations.

The generated mutations are:

-   `createPost`: Create a single Post.
-   `updatePost`: Update a single Post.
-   `upsertPost`: Update existing OR create single Post.
-   `deletePost`: Delete a single Post.
-   `createManyPosts`: Create multiple Posts.
-   `updateManyPosts`: Update multiple Posts.
-   `deleteManyPosts`: Delete multiple Posts.

### Creating a single Post

Single Post create mutations take one input:

-   `data`: `PostCreateInput!` A required object type specifying the data to create a new record.

**Standard create mutation**

```graphql
mutation {
    createPost(
        data: {
            authorId: 2
            title: "Foo"
            views: 2
            published: false
        }
    ) {
        id
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

**Advanced create mutation using relation queries**

<details><summary>List of all nested queries available</summary>
<p>

```graphql
author: {
    create: PostAuthorCreateInput, # Relation to one
    connect: PostAuthorWhereUniqueInput, # Relation to one
    connectOrCreate: PostAuthorConnectOrCreateInput # Relation to one
}
```

</p>
</details>

```graphql
mutation {
    createPost(
        data: {
            author: {
                connectOrCreate: {
                    where: PostWhereUniqueInput
                    create: PostCreateInput
                }
            }
        }
    ) {
        id
    }
}
```

### Updating a single Post

Single Post update mutations take two inputs:

-   `where`: `PostWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).
-   `data`: `PostUpdateInput!` A required object type specifying the data to update.

**Standard update mutation**

```graphql
mutation {
    updatePost(
        where: { id: 2 }
        data: {
            authorId: 2
            title: "Foo"
            views: 2
            published: false
        }
    ) {
        id
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

**Advanced update mutation using relation queries**

<details><summary>List of all nested queries available</summary>
<p>

```graphql
author: {
    create: PostAuthorCreateInput, # Relation to one
    connect: PostAuthorWhereUniqueInput, # Relation to one
    connectOrCreate: PostAuthorConnectOrCreateInput, # Relation to one
    update: PostAuthorUpdateInput, # Relation to one
    upsert: PostAuthorUpsertInput, # Relation to one
    delete: true,
    disconnect: true,
}
```

</p>
</details>

```graphql
mutation {
    updatePost(
        data: {
            author: {
                connectOrCreate: {
                    where: PostWhereUniqueInput
                    create: PostCreateInput
                }
            }
        }
    ) {
        id
    }
}
```

### Deleting a single Post

Single Post delete mutations take one input:

-   `where`: `PostWhereUniqueInput!` A required object type specifying a field with a unique constraint (like id).

**Standard delete mutation**

```graphql
mutation {
    deletePost(where: { id: 2 }) {
        id
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

### Creating multiple Posts

Multiple Posts create mutations take one input:

-   `data`: `[PostCreateManyInput!]` A required array specifying the data to create new records.
-   `skipDuplicates`: `Boolean` An optional Boolean specifying if unique fields or ID fields that already exist should be skipped.

**Standard deleteMany mutation**

```graphql
mutation {
    createManyPosts(
        data: [
            { title: "Foo" }
            { title: "Foo" }
            { title: "Foo" }
        ]
        skipDuplicates: true
    ) {
        count
    }
}
```

> `createManyPosts` returns an integer that represents the number of records that were created.

### Updating multiple Posts

Multiple Posts update mutations take two inputs:

-   `where`: `PostWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.
-   `data`: `PostUpdateInput!` A required object type specifying the data to update records with.

**Standard updateMany mutation**

```graphql
mutation {
    updateManyPosts(
        where: { title: "Foo" }
        data: { title: "Foo" }
    ) {
        count
    }
}
```

> `updateManyPosts` returns an integer that represents the number of records that were updated.

### Deleting multiple Posts

Multiple Posts delete mutations can take one input:

-   `where`: `PostWhereFilterInput!` A required object type to filter the content based on a nested set of criteria.

**Standard deleteMany mutation**

```graphql
mutation {
    deleteManyPosts(where: { title: "Foo" }) {
        count
    }
}
```

> `deleteManyPosts` returns an integer that represents the number of records that were deleted.

## Subscriptions

Subscriptions allows listen for data changes when a specific event happens, in real-time.

### Subscribing to a single Post creation

Triggered from `createPost` mutation (excl. `createManyPosts` and `upsertPost`).

```graphql
subscription {
    onCreatedPost {
        id
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

### Subscribing to a single Post update

Triggered from `updatePost` mutation (excl. `updateManyPosts` and `upsertPost`).

```graphql
subscription {
    onUpdatedPost {
        id
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

### Subscribing to a single Post upsert

Triggered from `upsertPost` mutation.

```graphql
subscription {
    onUpsertedPost {
        id
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

### Subscribing to a single Post deletion

Triggered from `deletePost` mutation (excl. `deleteManyPosts`).

```graphql
subscription {
    onDeletedPost {
        id
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

### Subscribing to a single Post mutation

Triggered from ANY SINGLE record mutation (excl. `on*ManyPosts`).

```graphql
subscription {
    onMutatedPost {
        id
        authorId
        title
        views
        published
        createdAt
        updatedAt
    }
}
```

### Subscribing to many Post creations

Triggered from `createManyPosts` mutation.

```graphql
subscription {
    onCreatedManyPosts {
        count
    }
}
```

### Subscribing to many Post updates

Triggered from `updateManyPosts` mutation.

```graphql
subscription {
    onUpdatedManyPosts {
        count
    }
}
```

### Subscribing to many Post deletions

Triggered from `deleteManyPosts` mutation.

```graphql
subscription {
    onDeletedManyPosts {
        count
    }
}
```

### Subscribing to many Post mutations

Triggered from ANY MULTIPLE records mutation (excl. single record mutations).

```graphql
subscription {
    onMutatedManyPosts {
        count
    }
}
```
