-- 1.1)
SELECT games.title, publishers.name FROM games
    INNER JOIN publishers ON (games.publisher_id = publishers.id)
    ORDER BY publisher_id;
-- 1.2)
SELECT users.username, profiles.bio AS bio FROM users
    INNER JOIN profiles ON (users.id = profiles.user_id)
    ORDER BY users.id;
-- 1.3)
SELECT users.username, games.title, user_games.hours_played FROM users
    INNER JOIN user_games ON user_games.user_id = users.id
    INNER JOIN games ON user_games.game_id = games.id
    ORDER BY users.username;
-- 1.4)
SELECT users.username, games.title, reviews.rating, reviews.comment FROM users
    INNER JOIN reviews ON reviews.user_id = users.id
    INNER JOIN games ON reviews.game_id = games.id
    ORDER BY users.username;
-- 1.5)
SELECT users.username, games.title, user_games.purchase_date FROM users
    INNER JOIN user_games ON user_games.user_id = users.id
    INNER JOIN games ON user_games.game_id = games.id
    ORDER BY users.username, user_games.purchase_date;
-- 2.1)
SELECT users.*, profiles.* FROM users
    LEFT JOIN profiles ON users.id = profiles.user_id
    ORDER BY users.id;
-- 2.2)
SELECT games.*, reviews.* FROM games
    LEFT JOIN reviews ON games.id = reviews.game_id
    ORDER BY games.id;
-- 2.3)
SELECT publishers.*, games.* FROM publishers
    LEFT JOIN games ON publishers.id = games.publisher_id
    ORDER BY publishers.id;
-- 2.4)
SELECT * FROM users
    LEFT JOIN user_games ON users.id = user_games.user_id
    LEFT JOIN games ON user_games.game_id = games.id
    WHERE user_games.user_id IS NULL 
    ORDER BY users.id;
-- 2.5)
SELECT * FROM games
    LEFT JOIN user_games ON games.id = user_games.game_id
    LEFT JOIN users ON user_games.user_id = user_games.user_id
    WHERE user_games.game_id IS NULL 
    ORDER BY games.id;
-- 3.1)
SELECT games.title, COUNT(user_games.user_id) FROM games
    LEFT JOIN user_games ON games.id = user_games.game_id
    GROUP BY games.id
    ORDER BY games.title;
-- 3.2)
SELECT games.title, AVG(reviews.rating) FROM games
    LEFT JOIN reviews ON games.id = reviews.game_id
    GROUP BY games.id
    ORDER BY games.title;
-- 3.3)
SELECT games.title, SUM(user_games.hours_played) FROM games
    LEFT JOIN user_games ON games.id = user_games.game_id
    GROUP BY games.id
    ORDER BY games.title;
-- 3.4)
SELECT users.username, COUNT(user_games.game_id) FROM users
    LEFT JOIN user_games ON users.id = user_games.user_id
    GROUP BY users.id
    ORDER BY users.username;