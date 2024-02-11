CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type INTEGER,
    password_hash TEXT,
    address TEXT,

    approved BOOL DEFAULT NULL,
    pending BOOL DEFAULT TRUE,
    
    created INTEGER,
    updated INTEGER
);

CREATE TABLE user_applications (
    user_id INTEGER PRIMARY KEY,
    
    approved BOOL DEFAULT NULL,
    pending BOOL DEFAULT TRUE,

    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE user_usernames (
    user_id INTEGER PRIMARY KEY,
    username TEXT UNIQUE,

    created INTEGER,
    updated INTEGER,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE user_emails (
    user_id INTEGER PRIMARY KEY,
    email TEXT,

    created INTEGER,
    updated INTEGER,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE user_phones (
    user_id INTEGER PRIMARY KEY,
    phone TEXT,

    created INTEGER,
    updated INTEGER,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE memberships (
    user_id INTEGER PRIMARY KEY,
    club_id INTEGER,

    approved BOOL DEFAULT NULL,
    pending BOOL DEFAULT TRUE,

    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
    FOREIGN KEY (club_id) REFERENCES clubs(id)
);

CREATE TABLE clubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,

    approved BOOL DEFAULT NULL,
    pending BOOL DEFAULT TRUE,

    coordinator INTEGER,
    
    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (coordinator) REFERENCES users(id)
);

CREATE TABLE club_applications (
    club_id INTEGER PRIMARY KEY,
    
    approved BOOL DEFAULT NULL,
    pending BOOL DEFAULT TRUE,

    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (club_id) REFERENCES clubs(id)
);

CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,
    event_start DATETIME,
    event_end DATETIME,
    venue_id INTEGER,
    
    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (club_id) REFERENCES clubs (id),
    FOREIGN KEY (venue_id) REFERENCES venues (id)
);

CREATE TABLE event_applications (
    event_id INTEGER PRIMARY KEY,
    user_id INTEGER,

    approved BOOL DEFAULT NULL,
    pending BOOL DEFAULT TRUE,

    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,
    venue TEXT,
    
    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (club_id) REFERENCES clubs (id)
);