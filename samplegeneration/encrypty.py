import bcrypt
import csv


def encrypt_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12)).decode("utf-8")

pathToCSV = r"MOCK_DATA.csv"

begin = "BEGIN;"
commit = "COMMIT;"

# BEGIN;
# INSERT INTO users(type, password_hash, address, approved)
# VALUES (2,'$2b$12$Sry4C/f2kvMtTmGsnU.9FednX200gSPyuw4LQkzwOha7HY5CL4X.q','Admin town Adminland',true);

# INSERT INTO user_email (user_id, email)
#   VALUES(LAST_INSERT_ID(),'EMAIL');

# INSERT INTO user_phone (user_id, phone)
#   VALUES(LAST_INSERT_ID(),'PHONE NUMBER');

# INSERT INTO user_username (user_id, username)
#   VALUES(LAST_INSERT_ID(),'USERNAME');

# COMMIT;

inserts = []

# Open the file and read the contents
with open(pathToCSV, "r") as file:
    csvData = csv.reader(file)

    for index, row in enumerate(csvData):
        if index == 0:
            continue

        # create the insert statements
        userInsert = f"INSERT INTO users (type, password_hash, address) VALUES ({row[1]}, '{encrypt_password(row[2])}', '{row[3]}');"
        applicationInsert = "INSERT INTO user_applications (user_id, approved, pending) VALUES ((SELECT last_insert_rowid()), TRUE, FALSE);"
        emailInsert = f"INSERT INTO user_emails (user_id, email) VALUES((SELECT last_insert_rowid()),'{row[4]}');"
        phoneInsert = f"INSERT INTO user_phones (user_id, phone) VALUES((SELECT last_insert_rowid()),'{row[5]}');"
        usernameInsert = f"INSERT INTO user_usernames (user_id, username) VALUES((SELECT last_insert_rowid()),'{row[0]}');"

        # sql command is the combination of the 4 insert statements + begin and commit
        sqlcommand = begin + "\n" + userInsert + "\n" + applicationInsert + "\n" + emailInsert + "\n" + phoneInsert + "\n" + usernameInsert + "\n" + commit
        inserts.append(sqlcommand)

# write the sql commands to a file
with open("final_insert_statements.sql", "w") as file:
    for insert in inserts:
        file.write(insert + "\n")
