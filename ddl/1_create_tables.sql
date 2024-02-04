CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    type INTEGER,
    password_hash TEXT,
    address TEXT,
    registered BOOL,
    
    -- SQLite doesn't have a DATETIME type.
    -- To get around this: all the fields storing datetimes
    -- are represented with an INTEGER storing a unix timestamp
    -- (number of seconds since 01/01/1970)
    created INTEGER,
    updated INTEGER
);

CREATE TABLE memberships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    club_id INTEGER,
    approved BOOL,
    
    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE clubs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT,
    validity BOOL,
    coordinator INTEGER,
    
    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (coordinator) REFERENCES users(id)
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

CREATE TABLE venues (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    club_id INTEGER,
    venue TEXT,
    
    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (club_id) REFERENCES clubs (id)
);

CREATE TABLE event_applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id INTEGER,
    user_id INTEGER,
    approved BOOL,

    created INTEGER,
    updated INTEGER,
    
    FOREIGN KEY (event_id) REFERENCES events (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE user_email (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    email TEXT,

    created INTEGER,
    updated INTEGER,

    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE TABLE user_phone (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    phone TEXT,

    created INTEGER,
    updated INTEGER,

    FOREIGN KEY (user_id) REFERENCES users (id)
);