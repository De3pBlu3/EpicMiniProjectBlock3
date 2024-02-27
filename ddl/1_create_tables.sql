CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type INTEGER NOT NULL,
    password_hash TEXT NOT NULL,
    address TEXT NOT NULL,

    created DATETIME,
    updated DATETIME
);

CREATE TABLE user_applications (
    user_id INTEGER PRIMARY KEY,
    
    approved BOOL DEFAULT FALSE NOT NULL,
    pending BOOL DEFAULT TRUE NOT NULL,

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

    approved BOOL DEFAULT FALSE NOT NULL,
    pending BOOL DEFAULT TRUE NOT NULL,

    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (club_id) REFERENCES clubs(id)
);

CREATE TABLE clubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,

    coordinator INTEGER,
    
    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (coordinator) REFERENCES users(id)
);

CREATE TABLE club_names (
    club_id INTEGER PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (club_id) REFERENCES clubs (id)
);

CREATE TABLE club_applications (
    club_id INTEGER PRIMARY KEY,

    approved BOOL DEFAULT FALSE NOT NULL,
    pending BOOL DEFAULT TRUE NOT NULL,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (club_id) REFERENCES clubs(id)
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,

    title TEXT NOT NULL,
    description TEXT NOT NULL,

    event_start DATETIME NOT NULL,
    event_end DATETIME NOT NULL,
    venue_id INTEGER,
    
    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (club_id) REFERENCES clubs (id),
    FOREIGN KEY (venue_id) REFERENCES venues (id)
);

CREATE TABLE event_attendance_applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    
    event_id INTEGER,
    user_id INTEGER,

    approved BOOL DEFAULT FALSE NOT NULL,
    pending BOOL DEFAULT TRUE NOT NULL,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,
    venue TEXT NOT NULL,

    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (club_id) REFERENCES clubs (id)
);