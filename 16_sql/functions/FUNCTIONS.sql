-- 1.1)
SELECT UPPER(users.username) FROM users;
-- 1.2)
SELECT users.username, LENGTH(users.username) FROM users;
-- 1.3)
SELECT games.title, EXTRACT(YEAR FROM games.release_date) FROM games;
-- 1.4)
SELECT *,
    CASE
        WHEN profiles.bio IS NULL THEN 'No bio yet'
        ELSE profiles.bio
    END
FROM profiles;
-- 1.5)
SELECT *,
    CASE
        WHEN games.price = 0 THEN 'Free'
        ELSE 'Paid'
    END AS price_label
FROM games;
-- 2.1)
SELECT COUNT(*) FROM users;
-- 2.2)
SELECT COUNT(*) FROM games;
-- 2.3)
SELECT AVG(gameS.price)::DECIMAL(10,2) FROM games;
-- 2.4)
SELECT SUM(hours_played) FROM user_games;
-- 2.5)
SELECT MIN(reviews.rating), MAX(reviews.rating) FROM reviews;
-- 3.1)
SELECT COUNT(*), users.country FROM users
    GROUP BY users.country;
-- 3.2)
SELECT COUNT(*), games.publisher_id FROM games
    GROUP BY games.publisher_id
    ORDER BY games.publisher_id;
-- 3.3)
SELECT  games.publisher_id, AVG(games.price) FROM games
    GROUP BY games.publisher_id
    ORDER BY games.publisher_id;
-- 3.4)
SELECT  user_games.user_id, SUM(user_games.hours_played) FROM user_games
    GROUP BY user_games.user_id
    ORDER BY user_games.user_id;
-- 3.5)
SELECT user_games.user_id, AVG(user_games.hours_played)::INT FROM user_games
    GROUP BY user_games.user_id
    ORDER BY user_games.user_id;
-- 3.6)
SELECT  user_games.game_id, SUM(user_games.hours_played) FROM user_games
    GROUP BY user_games.game_id
    ORDER BY user_games.game_id;
-- 3.7)
SELECT  user_games.game_id, AVG(user_games.hours_played)::INT FROM user_games
    GROUP BY user_games.game_id
    ORDER BY user_games.game_id;
-- 3.8)
SELECT EXTRACT(YEAR FROM user_games.purchase_date) AS purchased_year, COUNT(*) FROM user_games
    GROUP BY purchased_year
    ORDER BY purchased_year;
-- 3.9)
SELECT EXTRACT(YEAR FROM games.release_date) AS release_year, COUNT(*) FROM games
    GROUP BY release_year
    ORDER BY release_year;
-- 3.10)
SELECT COUNT(*),
    CASE
        WHEN games.price = 0 THEN 'Free'
        ELSE 'Paid'
    END AS price_label
    FROM games
    GROUP BY price_label
    ORDER BY price_label;
-- 4.1)
SELECT COUNT(games.price) AS paid_games, games.publisher_id FROM games
    WHERE games.price > 0
    GROUP BY games.publisher_id
    ORDER BY games.publisher_id;
-- 4.2)
SELECT AVG(games.price), games.publisher_id FROM games
    WHERE games.release_date > '2015-01-01'
    GROUP BY games.publisher_id
    ORDER BY games.publisher_id;
-- 5.1)
SELECT users.country, COUNT(users.id) FROM users
    GROUP BY users.country
    HAVING COUNT(users.id) > 0
    ORDER BY users.country;
-- 5.2)
SELECT user_games.user_id, SUM(user_games.hours_played) FROM user_games
    GROUP BY user_games.user_id
    HAVING SUM(user_games.hours_played) > 300
    ORDER BY user_games.user_id;
-- 5.3)
SELECT reviews.game_id, AVG(reviews.rating) FROM reviews
    GROUP BY reviews.game_id
    HAVING AVG(reviews.rating) > 4.5
    ORDER BY reviews.game_id