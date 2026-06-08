-- 1)
SELECT * FROM games
    WHERE games.price > (
        SELECT AVG(games.price) FROM games
    );
-- 2)
WITH average_playtime AS(
    SELECT SUM(user_games.hours_played) AS hours_played FROM user_games
    GROUP BY user_games.user_id
)
SELECT users.username FROM users
    WHERE users.id IN (
        SELECT user_games.user_id FROM user_games
        GROUP BY user_games.user_id
        HAVING SUM(user_games.hours_played) > (
            SELECT AVG(average_playtime.hours_played) FROM average_playtime
        )
    )
    ORDER BY users.username;
-- 3)
SELECT games.title FROM games
    WHERE games.id IN (
        SELECT reviews.game_id FROM reviews
        GROUP BY reviews.game_id
        HAVING COUNT(reviews.user_id) > 0
    )
    ORDER BY games.title;
-- 4)
SELECT games.title FROM games
    WHERE games.id NOT IN (
        SELECT reviews.game_id FROM reviews
        GROUP BY reviews.game_id
        HAVING COUNT(reviews.user_id) > 0
    )
    ORDER BY games.title;
-- 5)
SELECT users.username FROM users
    WHERE users.id IN (
        SELECT user_games.user_id FROM user_games
        GROUP BY user_games.user_id
        HAVING COUNT(user_games.game_id) > 0
    )
    ORDER BY users.username;
-- 6)
SELECT users.username FROM users
    WHERE users.id NOT IN (
        SELECT user_games.user_id FROM user_games
        GROUP BY user_games.user_id
        HAVING COUNT(user_games.game_id) > 0
    )
    ORDER BY users.username;
-- 7)
SELECT games.title FROM games
    WHERE games.price = (
        SELECT MAX(games.price) FROM games
    );
-- 8)
SELECT publishers.name FROM publishers
    WHERE publishers.id IN (
        SELECT games.publisher_id FROM games
            WHERE games.price = 0
    );
-- 9)
SELECT users.username FROM users
    WHERE users.id IN (
        SELECT user_games.user_id FROM user_games
        WHERE user_games.game_id IN (
            SELECT games.id FROM games
            WHERE games.id = (
                SELECT publishers.id FROM publishers
                WHERE publishers.name = 'Rockstar Games'
            )
        )
    )
    ORDER BY users.username;
-- 10)
SELECT users.username FROM users
    WHERE users.id IN (
        SELECT reviews.user_id FROM reviews
            WHERE reviews.game_id NOT IN (
                SELECT user_games.game_id FROM user_games
                WHERE user_games.user_id = users.id
            )
    )
    ORDER BY users.username;
-- 11)
WITH total_playtime AS(
    SELECT user_games.user_id, SUM(user_games.hours_played) AS hours_played FROM user_games
    GROUP BY user_games.user_id
    ORDER BY hours_played DESC
    LIMIT 3
)
SELECT users.username, total_playtime.hours_played FROM users
    INNER JOIN total_playtime ON users.id = total_playtime.user_id
    WHERE users.id IN (
        SELECT total_playtime.user_id FROM total_playtime
    );
-- 12)
WITH publisher_games
    AS(
        SELECT games.publisher_id, COUNT(games.id), AVG(games.price)::DECIMAL(10,2) FROM games
        GROUP BY games.publisher_id
        HAVING COUNT(games.id) > 1
    )
SELECT publishers.name, publisher_games.count, publisher_games.avg from publishers
    INNER JOIN publisher_games ON publishers.id = publisher_games.publisher_id
    WHERE publishers.id IN (
        SELECT publisher_games.publisher_id FROM publisher_games
    );
-- 13)
-- PAS BON, perds les infos sur les jeux sans reviews ou sans user
WITH player_data AS(
    SELECT user_games.game_id, COUNT(DISTINCT user_games.user_id) AS players, SUM(DISTINCT user_games.hours_played) AS playtime, AVG(DISTINCT reviews.rating) AS rating FROM user_games
    LEFT JOIN reviews ON user_games.game_id = reviews.game_id
    GROUP BY user_games.game_id
)
SELECT games.title, publishers.name, COALESCE(player_data.players, 0), COALESCE(player_data.playtime, 0), COALESCE(player_data.rating, 0) FROM games
    LEFT JOIN player_data ON games.id = player_data.game_id
    INNER JOIN publishers ON games.publisher_id = publishers.id;
-- 14)
WITH game_data AS(
    SELECT games.publisher_id, COUNT(DISTINCT games.id) AS game, AVG(DISTINCT games.price) AS price, SUM(DISTINCT user_games.hours_played) AS playtime FROM games
        LEFT JOIN user_games ON games.id = user_games.game_id
        GROUP BY games.publisher_id
)
SELECT publishers.name, COALESCE(game_data.game, 0), COALESCE(game_data.price, 0), COALESCE(game_data.playtime, 0) FROM publishers
    LEFT JOIN game_data ON publishers.id = game_data.publisher_id;
-- 15)
WITH publisher_prices AS(
    SELECT publishers.id, publishers.name, AVG(DISTINCT games.price) AS price FROM games
        INNER JOIN publishers ON publishers.id = games.publisher_id
        GROUP BY publishers.id, publishers.name
)
SELECT games.title, games.price, publisher_prices.name FROM games
    INNER JOIN publisher_prices ON games.publisher_id = publisher_prices.id
    WHERE games.price > (
        SELECT publisher_prices.price FROM publisher_prices
        WHERE games.publisher_id = publisher_prices.id
    );