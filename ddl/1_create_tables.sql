CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type INTEGER,
    password_hash TEXT,
    address TEXT,

    created DATETIME,
    updated DATETIME
);

CREATE TABLE user_applications (
    user_id INTEGER PRIMARY KEY,
    
    approved BOOL DEFAULT FALSE,
    pending BOOL DEFAULT TRUE,

    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE user_usernames (
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE NOT NULL,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE user_emails (
    user_id INTEGER PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE user_phones (
    user_id INTEGER PRIMARY KEY,
    phone TEXT UNIQUE NOT NULL,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE memberships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    club_id INTEGER,

    approved BOOL DEFAULT FALSE,
    pending BOOL DEFAULT TRUE,

    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (club_id) REFERENCES clubs(id)
);

CREATE TABLE clubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,

    coordinator INTEGER,
    
    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (coordinator) REFERENCES users(id)
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,
    event_start DATETIME,
    event_end DATETIME,
    venue_id INTEGER,
    
    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (club_id) REFERENCES clubs (id),
    FOREIGN KEY (venue_id) REFERENCES venues (id)
);

CREATE TABLE event_attendance_applications (
    event_id INTEGER PRIMARY KEY,
    user_id INTEGER,

    approved BOOL DEFAULT FALSE,
    pending BOOL DEFAULT TRUE,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,
    venue TEXT,
    
    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (club_id) REFERENCES clubs (id)
);