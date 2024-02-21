/*
    forbid_delete_admin
    "The first registered user becomes the admin coordinator, a non-deletable account"
*/

CREATE TRIGGER forbid_delete_admin BEFORE DELETE ON users
FOR EACH ROW
-- type of 2 = admin
WHEN OLD.type = 2 
BEGIN
    SELECT RAISE(ABORT, 'Admin user cannot be deleted');
END;

CREATE TRIGGER forbid_deprivilege_admin BEFORE UPDATE ON users
FOR EACH ROW
WHEN OLD.type = 2 AND (NEW.type != 2 OR NOT (SELECT approved FROM user_applications WHERE user_id=NEW.id LIMIT 1))
BEGIN
    SELECT RAISE(ABORT, 'Admin user cannot be deprivileged or deregistered');
END;

/*
    forbid_more_than_three_memberships
    "Users can request/join a maximum of three clubs"

    Note: SQlite does not allow for a trigger to be fired on both the insertion
    and updating of a row - hence two near-identical triggers
*/

CREATE TRIGGER forbid_more_than_three_memberships_insert BEFORE INSERT ON memberships
FOR EACH ROW
WHEN (
    SELECT COUNT(*) from memberships WHERE user_id = NEW.user_id
) = 4
BEGIN
    SELECT RAISE(ABORT, 'A user cannot have more than three memberships');
END;

CREATE TRIGGER forbid_more_than_three_memberships_update BEFORE UPDATE ON memberships
FOR EACH ROW
WHEN (
    SELECT COUNT(*) from memberships WHERE user_id = NEW.user_id
) = 4
BEGIN
    SELECT RAISE(ABORT, 'A user cannot have more than three memberships');
END;

/*
    autodelete users when both pending and is approved is false 
    Aka When the user is rejected
*/

CREATE TRIGGER delete_user_if_rejected
AFTER UPDATE OF approved, pending ON user_applications
FOR EACH ROW
WHEN NEW.approved = 0 AND NEW.pending = 0
BEGIN
    DELETE FROM user_phones WHERE user_id = NEW.user_id;
    DELETE FROM user_usernames WHERE user_id = NEW.user_id;
    DELETE FROM user_emails WHERE user_id = NEW.user_id;
    DELETE FROM memberships WHERE user_id = NEW.user_id;
    DELETE FROM event_attendance_applications WHERE user_id = NEW.user_id;
    DELETE FROM users WHERE id = NEW.user_id;
END;