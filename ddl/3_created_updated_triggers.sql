-- Generated automatically by generate_created_updated_triggers.py
CREATE TRIGGER users_created_timestamp AFTER INSERT ON users
BEGIN
    UPDATE users SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER users_updated_timestamp AFTER UPDATE ON users
BEGIN
    UPDATE users SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER memberships_created_timestamp AFTER INSERT ON memberships
BEGIN
    UPDATE memberships SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER memberships_updated_timestamp AFTER UPDATE ON memberships
BEGIN
    UPDATE memberships SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER clubs_created_timestamp AFTER INSERT ON clubs
BEGIN
    UPDATE clubs SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER clubs_updated_timestamp AFTER UPDATE ON clubs
BEGIN
    UPDATE clubs SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER events_created_timestamp AFTER INSERT ON events
BEGIN
    UPDATE events SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER events_updated_timestamp AFTER UPDATE ON events
BEGIN
    UPDATE events SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER venues_created_timestamp AFTER INSERT ON venues
BEGIN
    UPDATE venues SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER venues_updated_timestamp AFTER UPDATE ON venues
BEGIN
    UPDATE venues SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER event_applications_created_timestamp AFTER INSERT ON event_applications
BEGIN
    UPDATE event_applications SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER event_applications_updated_timestamp AFTER UPDATE ON event_applications
BEGIN
    UPDATE event_applications SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_email_created_timestamp AFTER INSERT ON user_email
BEGIN
    UPDATE user_email SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_email_updated_timestamp AFTER UPDATE ON user_email
BEGIN
    UPDATE user_email SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_phone_created_timestamp AFTER INSERT ON user_phone
BEGIN
    UPDATE user_phone SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_phone_updated_timestamp AFTER UPDATE ON user_phone
BEGIN
    UPDATE user_phone SET updated = unixepoch('now') WHERE id = NEW.id;
END;
