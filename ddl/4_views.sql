CREATE VIEW all_user_info AS
    SELECT users.id, username, type, email, address, phone, approved, pending
    FROM users
    INNER JOIN user_emails ON users.id = user_emails.user_id
    INNER JOIN user_phones ON users.id = user_phones.user_id
    INNER JOIN user_usernames ON users.id = user_usernames.user_id
    INNER JOIN user_applications ON users.id = user_applications.user_id;


CREATE VIEW all_club_info AS 
    SELECT clubs.id, clubs.description, club_names.name, club_applications.approved, club_applications.pending, user_usernames.username
    FROM clubs
    INNER JOIN club_names ON clubs.id = club_names.club_id
    INNER JOIN club_applications ON clubs.id = club_applications.club_id
    INNER JOIN user_usernames ON clubs.coordinator = user_usernames.user_id