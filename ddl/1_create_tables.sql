CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    type INTEGER,
    password_hash TEXT,
    address TEXT,
    registered BOOL,
    
    created DATETIME,
    updated DATETIME
);

CREATE TABLE memberships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    club_id INTEGER,
    approved BOOL,
    
    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE clubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    validity BOOL,
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

CREATE TABLE venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,
    venue TEXT,
    
    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (club_id) REFERENCES clubs (id)
);

CREATE TABLE event_applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER,
    user_id INTEGER,
    approved BOOL,

    created DATETIME,
    updated DATETIME,
    
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE user_email (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    email TEXT,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE user_phone (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    phone TEXT,

    created DATETIME,
    updated DATETIME,

    FOREIGN KEY (user_id) REFERENCES users (id)
);