# SQLAlchemy Project — Steam Lite

## Objective

The goal of this project is to recreate a simplified Steam-like platform using SQLAlchemy.

You must:

* Create database models
* Define relationships
* Create the database
* Seed test data
* Implement business rules
* Execute queries using SQLAlchemy

---

# Part 1 — Models

## Gender

Create an Enum containing:

* Male
* Female
* Other

---

## User

A user contains:

* id
* username
* email
* gender

### Business Rules

* username is required
* email is required
* email must be unique
* gender must be a valid value from the Gender enum

---

## Profile

A profile contains:

* id
* user_id
* bio
* country
* birth_date
* avatar_url

### Business Rules

* A user can only have one profile

---

## Publisher

A publisher contains:

* id
* name
* country

### Business Rules

* name is required
* name must be unique

---

## Game

A game contains:

* id
* title
* price
* release_date
* publisher_id

## AgeRating

Create an Enum containing:

- PEGI_3
- PEGI_7
- PEGI_12
- PEGI_16
- PEGI_18

### Business Rules

* title is required
* title must be unique
* price cannot be negative
* every game belongs to one publisher

---

## UserGame

Represents a purchased game.

Contains:

* user_id
* game_id
* purchase_date
* hours_played

### Business Rules

* a user cannot buy the same game twice
* hours_played cannot be negative

---

## Review

A review contains:

* id
* user_id
* game_id
* rating
* comment

### Business Rules

* rating must be between 1 and 5
* a user can only review a game once

---

# Part 2 — Relationships

Implement all relationships using:

* ForeignKey
* relationship
* back_populates

Required relationships:

### User ↔ Profile

One User has one Profile.

### Publisher ↔ Game

One Publisher has many Games.

### User ↔ UserGame

One User has many purchased games.

### Game ↔ UserGame

One Game can be owned by many users.

### User ↔ Review

One User can write many Reviews.

### Game ↔ Review

One Game can receive many Reviews.

---

# Part 3 — Database Creation

Create:

* Engine
* Session
* Tables

The application must create the database automatically.

---

# Part 4 — Seed Data

Insert enough data to test every feature.

Minimum:

* 10 Users
* 10 Profiles
* 5 Publishers
* 20 Games
* 30 Purchases
* 15 Reviews

---

# Part 5 — Business Logic

## Create User

Create a new user.

Rules:

* username required
* email unique

---

## Create Game

Create a new game.

Rules:

* title unique
* valid publisher

---

## Buy Game

Function:

buy_game(user_id, game_id)

Rules:

* user must exist
* game must exist
* user cannot buy the same game twice
* the user must be old enough to buy the game according to the game's age rating

Creates a UserGame entry.

---

## Play Game

Function:

play_game(user_id, game_id, hours)

Rules:

* user must own the game
* hours must be positive

Adds hours to UserGame.hours_played.

---

## Review Game

Function:

review_game(user_id, game_id, rating, comment)

Rules:

* user must own the game
* rating between 1 and 5
* user cannot review the same game twice

---

## Refund Game

Function:

refund_game(user_id, game_id)

Rules:

* purchase must exist

Deletes the UserGame entry.

---

## Update Profile

Function:

update_profile(...)

Allows updating:

* bio
* country
* avatar_url

---

# Part 6 — Queries

Implement the following SQLAlchemy queries.

### Query 1

Display all users.

---

### Query 2

Display all games.

---

### Query 3

Display all publishers.

---

### Query 4

Display all games of a given publisher.

---

### Query 5

Display all games owned by a user.

---

### Query 6

Display all reviews of a game.

---

### Query 7

Display all games costing more than 30€.

---

### Query 8

Display all users who own more than 2 games.

---

### Query 9

Display the number of purchases per game.

---

### Query 10

Display the average rating per game.

---

### Query 11

Display the top 5 most purchased games.

---

### Query 12

Display the top 5 users with the most total hours played.

---

### Query 13

Display all users with:

* username
* total games owned
* total hours played

---

### Query 14

Display all games with:

* title
* total players
* total hours played

---

### Query 15

Display all publishers with:

* publisher name
* total games
* average game price

---

# Bonus

### Bonus 1

Display games that have never been purchased.

---

### Bonus 2

Display users who never wrote a review.

---

### Bonus 3

Display all users grouped by gender.

---

### Bonus 4

Display the average hours played per user.

---

### Bonus 5

Display the highest rated game.

---

# Deliverables

Your project must contain:

* Models
* Relationships
* Database creation
* Seed script
* Business functions
* Query functions

The application must run without errors and demonstrate proper usage of SQLAlchemy ORM.
