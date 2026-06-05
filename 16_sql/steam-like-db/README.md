# Entity-Relationship Modeling Exercise — Gaming Platform

We want to create a small gaming platform similar to Steam.

The platform must support the following features:

- Users can create an account with a username, email and country.
- Each user can have a profile containing:
  - a bio
  - an avatar
  - a birth date

- Games exist on the platform.
- Each game has:
  - a title
  - a price
  - a release date

- Games are created by publishers.
- A publisher can publish multiple games.

- Users can buy multiple games.
- A game can be owned by multiple users.
- We also want to store:
  - the purchase date
  - the number of hours played for each owned game

- Users can leave reviews on games.
- A review contains:
  - a rating
  - a comment
  - a creation date

---

## Tasks

1. Identify the entities.
2. Identify the attributes of each entity.
3. Identify the relationships between entities.
4. Determine the cardinalities:
   - one-to-one
   - one-to-many
   - many-to-many
5. Draw the Entity-Relationship diagram.
6. Translate the schema into relational tables.
