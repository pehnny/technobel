-- 1)
SELECT * FROM users;
-- 2)
SELECT users.username, users.country FROM users;
-- 3)
SELECT * FROM games;
-- 4)
SELECT games.title, games.price FROM games;
-- 5)
SELECT * FROM games
    WHERE games.price >= 40;
-- 6)
SELECT * from games
    WHERE games.price <= 50;
-- 7)
SELECT * FROM games
    WHERE games.price = 0;
-- 8)
SELECT * FROM users
    WHERE users.country ILIKE 'belgium';
-- 9)
SELECT * FROM users
    WHERE users.country NOT ILIKE 'belgium';
-- 10)
SELECT * FROM publishers
    WHERE publishers.country ILIKE 'USA';
-- 11)
SELECT * from games
    WHERE games.release_date > '2020-01-01';
-- 12)
SELECT * from games
    WHERE games.release_date < '2020-01-01';
-- 13)
SELECT * FROM games
    ORDER BY games.price DESC;
-- 14)
SELECT * FROM games
    ORDER BY games.price DESC;
-- 15)
SELECT users.username FROM users
    ORDER BY users.username;
-- 16)
SELECT * FROM games
    WHERE games.title LIKE '%Dark%';
-- 17)
SELECT * FROM games
    WHERE games.title LIKE 'C%';
-- 18)
SELECT * FROM users
    WHERE users.username LIKE '%a%';
-- 19)
SELECT * FROM reviews
    WHERE reviews.rating = 5;
-- 20)
SELECT * FROM reviews
    WHERE reviews.created_at > '2024-01-01';
-- 21)
SELECT * FROM games
    WHERE games.price BETWEEN 20 AND 60;
-- 22)
SELECT * FROM users
    WHERE users.country ILIKE 'belgium' OR users.country ILIKE 'france';
-- 23)
SELECT * FROM games
    WHERE games.price > 0;
-- 24)
SELECT * FROM games
    ORDER BY games.title;
-- 25)
SELECT * FROM publishers
    ORDER BY publishers.name;
-- 26)
SELECT * FROM games
    WHERE games.title LIKE '%2';
-- 27)

-- 28)
SELECT * FROM games
    WHERE games.release_date BETWEEN '2015-01-01' AND '2022-01-01';
-- 29)
SELECT * FROM reviews
    WHERE reviews.comment ILIKE '%best%';
-- 30)
SELECT * FROM games
    WHERE games.price = 59.99;