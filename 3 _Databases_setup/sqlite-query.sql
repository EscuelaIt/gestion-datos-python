SELECT * FROM sqlite_master;

CREATE TABLE IF NOT EXISTS accounts (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    created_at DATETIME NOT NULL,
    last_login DATETIME NOT NULL
);

INSERT INTO accounts (user_id, username, password, email, created_at, last_login)
VALUES (1, 'manduinca', '123456', 'manduinca@escuela.it', '2024-06-20', '2024-06-20');

SELECT * FROM accounts;
