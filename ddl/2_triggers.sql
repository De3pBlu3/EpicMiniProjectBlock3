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
) = 3
BEGIN
    SELECT RAISE(ABORT, 'A user cannot have more than three memberships');
END;

CREATE TRIGGER forbid_more_than_three_memberships_update BEFORE UPDATE ON memberships
FOR EACH ROW
WHEN (
    SELECT COUNT(*) from memberships WHERE user_id = NEW.user_id
) = 3
BEGIN
    SELECT RAISE(ABORT, 'A user cannot have more than three memberships');
END;