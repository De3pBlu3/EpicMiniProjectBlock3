INSERT INTO clubs (description, coordinator) VALUES
    ("Club A", 2),
    ("Club B", 3),
    ("Club C", 4);

INSERT INTO club_applications(club_id, approved, pending) VALUES
    (1, TRUE, FALSE),
    (2, TRUE, FALSE),
    (3, TRUE, FALSE);

INSERT INTO venues (club_id, venue) VALUES
    (1, "UL Sports Arena"),
    (2, "ISE Building"),
    (3, "Alison's Office");