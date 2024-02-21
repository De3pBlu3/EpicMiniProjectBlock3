
begin;
INSERT INTO clubs(description, coordinator) VALUES ('Club A description', 2);
insert into club_applications(club_id, approved, pending) values ((SELECT last_insert_rowid()), TRUE, FALSE);
insert into club_names(club_id, name) values ((SELECT last_insert_rowid()), 'Club A name');
commit;

begin;
INSERT INTO clubs(description, coordinator) VALUES ('Club B description', 3);
insert into club_applications(club_id, approved, pending) values ((SELECT last_insert_rowid()), TRUE, FALSE);
insert into club_names(club_id, name) values ((SELECT last_insert_rowid()), 'Club B name');
commit;

begin;
INSERT INTO clubs(description, coordinator) VALUES ('Club C description', 4);
insert into club_applications(club_id, approved, pending) values ((SELECT last_insert_rowid()), TRUE, FALSE);
insert into club_names(club_id, name) values ((SELECT last_insert_rowid()), 'Club C name');
commit;


insert into memberships (user_id, club_id) values (5, 1);
insert into memberships (user_id, club_id) values (5, 2);
insert into memberships (user_id, club_id) values (5, 3);
insert into memberships (user_id, club_id) values (6, 1);
insert into memberships (user_id, club_id) values (6, 2);
insert into memberships (user_id, club_id) values (7, 1);


INSERT INTO venues (club_id, venue) VALUES
    (1, "UL Sports Arena"),
    (2, "ISE Building"),
    (3, "Alison's Office");