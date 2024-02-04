INSERT INTO users(username, type, password_hash, address, registered) VALUES
    ('admin', 2, 'TODO: actual hashes', 'Admin Central, Adminland', TRUE),
    ('user',  0, 'TODO: actual hashes', 'User city', TRUE);

INSERT INTO clubs(description, validity, coordinator) VALUES 
    ('Club A', TRUE, 1),
    ('Club B', TRUE, 1),
    ('Club C', TRUE, 1);