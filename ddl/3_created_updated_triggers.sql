-- Generated automatically by generate_created_updated_triggers.py
CREATE TRIGGER users_created_timestamp AFTER INSERT ON users
BEGIN
    UPDATE users SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER users_updated_timestamp AFTER UPDATE ON users
BEGIN
    UPDATE users SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_applications_created_timestamp AFTER INSERT ON user_applications
BEGIN
    UPDATE user_applications SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_applications_updated_timestamp AFTER UPDATE ON user_applications
BEGIN
    UPDATE user_applications SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_usernames_created_timestamp AFTER INSERT ON user_usernames
BEGIN
    UPDATE user_usernames SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_usernames_updated_timestamp AFTER UPDATE ON user_usernames
BEGIN
    UPDATE user_usernames SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_emails_created_timestamp AFTER INSERT ON user_emails
BEGIN
    UPDATE user_emails SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_emails_updated_timestamp AFTER UPDATE ON user_emails
BEGIN
    UPDATE user_emails SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_phones_created_timestamp AFTER INSERT ON user_phones
BEGIN
    UPDATE user_phones SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_phones_updated_timestamp AFTER UPDATE ON user_phones
BEGIN
    UPDATE user_phones SET updated = unixepoch('now') WHERE id = NEW.id;
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

CREATE TRIGGER club_applications_created_timestamp AFTER INSERT ON club_applications
BEGIN
    UPDATE club_applications SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER club_applications_updated_timestamp AFTER UPDATE ON club_applications
BEGIN
    UPDATE club_applications SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER events_created_timestamp AFTER INSERT ON events
BEGIN
    UPDATE events SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER events_updated_timestamp AFTER UPDATE ON events
BEGIN
    UPDATE events SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER event_applications_created_timestamp AFTER INSERT ON event_applications
BEGIN
    UPDATE event_applications SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER event_applications_updated_timestamp AFTER UPDATE ON event_applications
BEGIN
    UPDATE event_applications SET updated = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER venues_created_timestamp AFTER INSERT ON venues
BEGIN
    UPDATE venues SET created = unixepoch('now') WHERE id = NEW.id;
END;

CREATE TRIGGER venues_updated_timestamp AFTER UPDATE ON venues
BEGIN
    UPDATE venues SET updated = unixepoch('now') WHERE id = NEW.id;
END;
