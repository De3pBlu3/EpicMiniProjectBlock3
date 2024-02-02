CREATE TABLE users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    type INT,
    password_hash TEXT,
    address TEXT,
    registered BOOL,
    created DATE,
    updated DATE
);

CREATE TABLE memberships (
    membership_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    club_id TEXT,
    approved BOOL,
    created DATE,
    updated DATE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE clubs (
    club_id TEXT PRIMARY KEY NOT NULL,
    description TEXT,
    validity BOOL,
    coordinator TEXT,
    created DATE,
    updated DATE,
    FOREIGN KEY (coordinator) REFERENCES users(user_id)
);

CREATE TABLE events (
    event_id TEXT PRIMARY KEY NOT NULL,
    club_id TEXT,
    event_start DATETIME,
    event_end DATETIME,
    venue_id TEXT,
    created DATE,
    updated DATE,
    FOREIGN KEY (club_id) REFERENCES clubs (club_id),
    FOREIGN KEY (venue_id) REFERENCES venue (venue_id)
);

CREATE TABLE venue (
    venue_id TEXT PRIMARY KEY,
    club_id TEXT,
    venue TEXT,
    created DATE,
    updated DATE,
    FOREIGN KEY (club_id) REFERENCES clubs (club_id)
);

CREATE TABLE event_applications (
    event_application_id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id TEXT,
    user_id INTEGER,
    approved BOOL,
    created DATE,
    updated DATE,
    FOREIGN KEY (event_id) REFERENCES events (event_id),
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE user_email (
    user_email_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    email TEXT,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);

CREATE TABLE user_phone (
    user_phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    phone TEXT,
    FOREIGN KEY (user_id) REFERENCES users (user_id)
);