# SQL Exercises — Gaming Platform
## JOINS / Advanced SELECT

### Part 1 — Basic JOIN

1. Display all games with the name of their publisher.

Expected columns:
- game_title
- publisher_name

2. Display all users with their profile bio.

Expected columns:
- username
- bio

3. Display all owned games.

Expected columns:
- username
- game_title
- hours_played

4. Display all reviews.

Expected columns:
- username
- game_title
- rating
- comment

5. Display all users with the games they own and the purchase date.

Expected columns:
- username
- game_title
- purchase_date

---

### Part 2 — LEFT JOIN

6. Display all users with their profiles.
Users without profiles must still appear.

7. Display all games with their reviews.
Games without reviews must still appear.

8. Display all publishers with their games.
Publishers without games must still appear.

9. Display all users who never bought a game.

10. Display all games that were never purchased.

---

### Part 3 — JOIN + GROUP BY

11. Display all games with their total number of players.

Expected columns:
- game_title
- total_players

12. Display the average rating for each reviewed game.

Expected columns:
- game_title
- average_rating

13. Display the total number of hours played for each game.

Expected columns:
- game_title
- total_hours_played

14. Display the total number of games owned by each user.

Expected columns:
- username
- total_games_owned

15. Display all publishers with the average price of their games.

Expected columns:
- publisher_name
- average_price

16. Display all users with:
- username
- number of owned games
- total hours played

---

### Part 4 — GROUP BY + HAVING

17. Display all users who own more than 2 games.

18. Display all publishers that published more than 1 game.

19. Display all games with an average rating greater than 4.

20. Display all users who wrote more than 1 review.

21. Display all games where the total played hours exceed 500.

---

### Part 5 — ORDER BY / LIMIT

22. Display users ordered by total hours played from highest to lowest.

23. Display the top 3 users with the most total hours played.

24. Display games ordered by total hours played from highest to lowest.

25. Display the top 5 most played games.

---

### Part 6 — More advanced JOIN + GROUP BY

26. Display all games with:
- title
- publisher name
- total players
- total hours played
- average rating

27. Display all users with:
- username
- owned games count
- reviews written count

28. Display all publishers with:
- publisher name
- total games
- average game price
- total hours played on their games

29. Display all games with:
- title
- publisher name
- total reviews
- average rating

Order the result by average rating descending.

30. Display all publishers ranked by total hours played on their games.

Expected columns:
- publisher_name
- total_hours_played
