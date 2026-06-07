-- 1.1)
SELECT
    games.title,
    publishers.name
FROM
    games
    INNER JOIN publishers ON (games.publisher_id = publishers.id)
ORDER BY
    publisher_id;

-- 1.2)
SELECT
    users.username,
    profiles.bio AS bio
FROM
    users
    INNER JOIN profiles ON (users.id = profiles.user_id)
ORDER BY
    users.id;

-- 1.3)
SELECT
    users.username,
    games.title,
    user_games.hours_played
FROM
    users
    INNER JOIN user_games ON user_games.user_id = users.id
    INNER JOIN games ON user_games.game_id = games.id
ORDER BY
    users.username;

-- 1.4)
SELECT
    users.username,
    games.title,
    reviews.rating,
    reviews.comment
FROM
    users
    INNER JOIN reviews ON reviews.user_id = users.id
    INNER JOIN games ON reviews.game_id = games.id
ORDER BY
    users.username;

-- 1.5)
SELECT
    users.username,
    games.title,
    user_games.purchase_date
FROM
    users
    INNER JOIN user_games ON user_games.user_id = users.id
    INNER JOIN games ON user_games.game_id = games.id
ORDER BY
    users.username,
    user_games.purchase_date;

-- 2.1)
SELECT
    users.*,
    profiles.*
FROM
    users
    LEFT JOIN profiles ON users.id = profiles.user_id
ORDER BY
    users.id;

-- 2.2)
SELECT
    games.*,
    reviews.*
FROM
    games
    LEFT JOIN reviews ON games.id = reviews.game_id
ORDER BY
    games.id;

-- 2.3)
SELECT
    publishers.*,
    games.*
FROM
    publishers
    LEFT JOIN games ON publishers.id = games.publisher_id
ORDER BY
    publishers.id;

-- 2.4)
SELECT
    *
FROM
    users
    LEFT JOIN user_games ON users.id = user_games.user_id
    LEFT JOIN games ON user_games.game_id = games.id
WHERE
    user_games.user_id IS NULL
ORDER BY
    users.id;

-- 2.5)
SELECT
    *
FROM
    games
    LEFT JOIN user_games ON games.id = user_games.game_id
    LEFT JOIN users ON user_games.user_id = user_games.user_id
WHERE
    user_games.game_id IS NULL
ORDER BY
    games.id;

-- 3.1)
SELECT
    games.title,
    COUNT(user_games.user_id)
FROM
    games
    LEFT JOIN user_games ON games.id = user_games.game_id
GROUP BY
    games.id
ORDER BY
    games.title;

-- 3.2)
SELECT
    games.title,
    AVG(reviews.rating)
FROM
    games
    LEFT JOIN reviews ON games.id = reviews.game_id
GROUP BY
    games.id
ORDER BY
    games.title;

-- 3.3)
SELECT
    games.title,
    SUM(user_games.hours_played)
FROM
    games
    LEFT JOIN user_games ON games.id = user_games.game_id
GROUP BY
    games.id
ORDER BY
    games.title;

-- 3.4)
SELECT
    users.username,
    COUNT(user_games.game_id)
FROM
    users
    LEFT JOIN user_games ON users.id = user_games.user_id
GROUP BY
    users.id
ORDER BY
    users.username;

-- 3.5)
SELECT
    publishers.name,
    AVG(games.price)
FROM
    publishers
    LEFT JOIN games ON publishers.id = games.publisher_id
GROUP BY
    publishers.id
ORDER BY
    publishers.name;

-- 3.6)
SELECT
    users.username,
    AVG(user_games.user_id),
    SUM(user_games.hours_played)
FROM
    users
    LEFT JOIN user_games ON users.id = user_games.user_id
GROUP BY
    users.id
ORDER BY
    users.username;

-- 4.1)
SELECT
    users.username,
    COUNT(user_games.game_id) AS owned_games
FROM
    users
    INNER JOIN user_games ON users.id = user_games.user_id
GROUP BY
    users.id
HAVING
    COUNT(user_games.game_id) > 2
ORDER BY
    users.username;

-- 4.2)
SELECT
    publishers.name,
    COUNT(games.publisher_id) AS published_games
FROM
    publishers
    INNER JOIN games ON publishers.id = games.publisher_id
GROUP BY
    publishers.id
HAVING
    COUNT(games.publisher_id) > 1
ORDER BY
    publishers.name;

-- 4.3)
SELECT
    games.title,
    AVG(reviews.rating) AS rating
FROM
    games
    INNER JOIN reviews ON games.id = reviews.game_id
GROUP BY
    games.id
HAVING
    AVG(games.publisher_id) > 4
ORDER BY
    rating DESC;

-- 4.4)
SELECT
    users.username,
    COUNT(reviews.user_id) AS reviews
FROM
    users
    INNER JOIN reviews ON users.id = reviews.user_id
GROUP BY
    users.id
HAVING
    COUNT(reviews.user_id) > 1
ORDER BY
    users.username DESC;

-- 4.5)
SELECT
    games.title,
    SUM(user_games.hours_played) AS total_playtime
FROM
    games
    INNER JOIN user_games ON games.id = user_games.user_id
GROUP BY
    games.id
HAVING
    SUM(user_games.hours_played) > 1
ORDER BY
    total_playtime DESC;

-- 5.1)
SELECT
    users.username,
    SUM(user_games.hours_played) AS playtime
FROM
    users
    INNER JOIN user_games ON users.id = user_games.user_id
GROUP BY
    users.id
ORDER BY
    playtime DESC;

-- 5.2)
SELECT
    users.username,
    SUM(user_games.hours_played) AS playtime
FROM
    users
    INNER JOIN user_games ON users.id = user_games.user_id
GROUP BY
    users.id
ORDER BY
    playtime DESC
LIMIT
    3;

-- 5.3)
SELECT
    games.title,
    SUM(user_games.hours_played) AS total_playtime
FROM
    games
    INNER JOIN user_games ON games.id = user_games.user_id
GROUP BY
    games.id
HAVING
    SUM(user_games.hours_played) > 1
ORDER BY
    total_playtime DESC;

-- 5.4)
SELECT
    games.title,
    SUM(user_games.hours_played) AS total_playtime
FROM
    games
    INNER JOIN user_games ON games.id = user_games.user_id
GROUP BY
    games.id
HAVING
    SUM(user_games.hours_played) > 1
ORDER BY
    total_playtime DESC
LIMIT
    5;

-- 6.1)
SELECT
    games.title,
    publishers.name AS publisher,
    COUNT(user_games.user_id) AS owners,
    SUM(user_games.hours_played) AS playtime,
    AVG(reviews.rating) AS rating
FROM
    games
    INNER JOIN publishers ON games.publisher_id = publishers.id
    INNER JOIN user_games ON games.id = user_games.game_id
    INNER JOIN reviews ON games.id = reviews.game_id
GROUP BY
    games.id,
    publishers.name
ORDER BY
    games.title;

-- 6.2)
SELECT
    users.username,
    COUNT(DISTINCT user_games.game_id) AS owned_games,
    COUNT(DISTINCT reviews.game_id) AS reviews
FROM
    users
    LEFT JOIN user_games ON users.id = user_games.user_id
    LEFT JOIN reviews ON user_games.user_id = reviews.user_id
GROUP BY
    users.id
ORDER BY
    users.username;

-- 6.3)
SELECT
    publishers.name,
    COUNT(DISTINCT games.id) AS games,
    AVG(DISTINCT games.price) AS avg_price,
    SUM(DISTINCT user_games.hours_played) AS playtime
FROM
    publishers
    INNER JOIN games ON publishers.id = games.publisher_id
    INNER JOIN user_games ON games.id = user_games.game_id
GROUP BY
    publishers.id
ORDER BY
    publishers.name;

-- 6.4)
SELECT
    games.title,
    publishers.name AS publisher,
    COUNT(reviews.game_id) AS reviews,
    AVG(reviews.rating) AS rating
FROM
    games
    INNER JOIN publishers ON games.publisher_id = publishers.id
    LEFT JOIN reviews ON games.id = reviews.game_id
GROUP BY
    games.id,
    publishers.id
ORDER BY
    games.title;

-- 6.5)
SELECT
    publishers.name,
    SUM(user_games.hours_played) AS playtime
FROM
    publishers
    LEFT JOIN games ON publishers.id = games.publisher_id
    LEFT JOIN user_games ON games.id = user_games.game_id
GROUP BY
    publishers.id
ORDER BY
    playtime DESC;
