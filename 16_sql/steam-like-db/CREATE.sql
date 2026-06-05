CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    username VARCHAR(64) NOT NULL UNIQUE,
    email VARCHAR(128) NOT NULL UNIQUE,
    birthdate DATE NOT NULL,
    country VARCHAR(64),
    created_at TIMESTAMPTZ DEFAULT NOW(),
    updated_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT username CHECK(LENGTH(username) > 3),
    CONSTRAINT email CHECK(email LIKE '%@%.%'),
    CONSTRAINT birthdate CHECK((EXTRACT(YEAR FROM AGE(NOW(), birthdate)) >= 18 AND EXTRACT(YEAR FROM birthdate) > 1900))
);

CREATE TABLE IF NOT EXISTS profiles (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    bio TEXT,
    avatar VARCHAR(256),
    user_id INT NOT NULL UNIQUE,
    CONSTRAINT fk_profils_users FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS publishers (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    publisher_name VARCHAR(64) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS games (
    id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    title VARCHAR(64) NOT NULL,
    price MONEY NOT NULL,
    release_date TIMESTAMPTZ DEFAULT NOW(),
    publisher_id INT,
    CONSTRAINT title CHECK(LENGTH(title) > 1),
    CONSTRAINT fk_games_publishers FOREIGN KEY (publisher_id) REFERENCES publishers(id)
    ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS libraries (
    user_id INT NOT NULL,
    game_id INT NOT NULL,
    playtime INT DEFAULT NULL,
    purchased_date TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT pk_libraries PRIMARY KEY (user_id, game_id),
    CONSTRAINT fk_libraries_users FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT fk_libraries_games FOREIGN KEY (game_id) REFERENCES games(id)
    ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS reviews (
    user_id INT,
    game_id INT NOT NULL,
    rating INT NOT NULL,
    comment TEXT NOT NULL,
    created_at TIMESTAMPTZ DEFAULT NOW(),
    CONSTRAINT pk_reviews PRIMARY KEY (user_id, game_id),
    CONSTRAINT fk_reviews_users FOREIGN KEY (user_id) REFERENCES users(id)
    ON UPDATE CASCADE ON DELETE SET NULL,
    CONSTRAINT fk_reviews_games FOREIGN KEY (game_id) REFERENCES games(id)
    ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT rating CHECK(rating BETWEEN 0 AND 5),
    CONSTRAINT comment CHECK(LENGTH(comment) > 1)
);