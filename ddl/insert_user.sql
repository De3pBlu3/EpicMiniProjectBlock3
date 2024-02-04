INSERT INTO users (username, password_hash) 
VALUES ("its_ushen", HASHBYTES('SHA2_512', "password"));