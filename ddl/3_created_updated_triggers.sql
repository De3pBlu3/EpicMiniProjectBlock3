-- Generated automatically by generate_created_updated_triggers.py
CREATE TRIGGER users_created_timestamp AFTER INSERT ON users
BEGIN
    UPDATE users SET created = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER users_updated_timestamp AFTER UPDATE ON users
BEGIN
    UPDATE users SET updated = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER user_applications_created_timestamp AFTER INSERT ON user_applications
BEGIN
    UPDATE user_applications SET created = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER user_applications_updated_timestamp AFTER UPDATE ON user_applications
BEGIN
    UPDATE user_applications SET updated = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER user_usernames_created_timestamp AFTER INSERT ON user_usernames
BEGIN
    UPDATE user_usernames SET created = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER user_usernames_updated_timestamp AFTER UPDATE ON user_usernames
BEGIN
    UPDATE user_usernames SET updated = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER user_emails_created_timestamp AFTER INSERT ON user_emails
BEGIN
    UPDATE user_emails SET created = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER user_emails_updated_timestamp AFTER UPDATE ON user_emails
BEGIN
    UPDATE user_emails SET updated = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER user_phones_created_timestamp AFTER INSERT ON user_phones
BEGIN
    UPDATE user_phones SET created = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER user_phones_updated_timestamp AFTER UPDATE ON user_phones
BEGIN
    UPDATE user_phones SET updated = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER memberships_created_timestamp AFTER INSERT ON memberships
BEGIN
    UPDATE memberships SET created = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER memberships_updated_timestamp AFTER UPDATE ON memberships
BEGIN
    UPDATE memberships SET updated = datetime('now') WHERE user_id = NEW.user_id;
END;

CREATE TRIGGER clubs_created_timestamp AFTER INSERT ON clubs
BEGIN
    UPDATE clubs SET created = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER clubs_updated_timestamp AFTER UPDATE ON clubs
BEGIN
    UPDATE clubs SET updated = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER events_created_timestamp AFTER INSERT ON events
BEGIN
    UPDATE events SET created = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER events_updated_timestamp AFTER UPDATE ON events
BEGIN
    UPDATE events SET updated = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER event_attendance_applications_created_timestamp AFTER INSERT ON event_attendance_applications
BEGIN
    UPDATE event_attendance_applications SET created = datetime('now') WHERE event_id = NEW.event_id;
END;

CREATE TRIGGER event_attendance_applications_updated_timestamp AFTER UPDATE ON event_attendance_applications
BEGIN
    UPDATE event_attendance_applications SET updated = datetime('now') WHERE event_id = NEW.event_id;
END;

CREATE TRIGGER venues_created_timestamp AFTER INSERT ON venues
BEGIN
    UPDATE venues SET created = datetime('now') WHERE id = NEW.id;
END;

CREATE TRIGGER venues_updated_timestamp AFTER UPDATE ON venues
BEGIN
    UPDATE venues SET updated = datetime('now') WHERE id = NEW.id;
END;
