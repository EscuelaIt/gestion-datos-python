/*

-- POSTGRES

SELECT datname FROM pg_database;
SELECT current_database();

*/

CREATE TABLE accounts (
    user_id INTEGER PRIMARY KEY,
    username VARCHAR (50) UNIQUE NOT NULL,
    password VARCHAR (50) NOT NULL,
    email VARCHAR (255) UNIQUE NOT NULL,
    created_at TIMESTAMP NOT NULL,
    last_login TIMESTAMP
);

INSERT INTO accounts (user_id, username, password, email, created_at, last_login)
VALUES (1, 'manduinca', '123456', 'manduinca@escuela.it', '2024-06-20', '2024-06-20');

SELECT * FROM accounts;