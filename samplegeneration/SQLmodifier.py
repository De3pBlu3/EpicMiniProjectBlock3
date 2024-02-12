import csv


pathToSql = r"samplegeneration/original_insert_statements.sql"

pathToCSV = r"samplegeneration/MOCK_DATA.csv"

begin = "BEGIN;"
commit = "COMMIT;"

data = []

# Open the file and read the contents
with open(pathToSql, "r") as file:
    data = file.readlines()


#BEGIN;
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


    for index, row  in enumerate(csvData):
        if row == 0:
            continue

        # create the insert statements
        userInsert = data[index - 1]
        emailInsert = f"INSERT INTO user_email (user_id, email) VALUES((SELECT LAST_INSERT_ID()),'{row[0]}');"
        phoneInsert = f"INSERT INTO user_phone (user_id, phone) VALUES((SELECT LAST_INSERT_ID()),'{row[1]}');"
        usernameInsert = f"INSERT INTO user_username (user_id, username) VALUES((SELECT LAST_INSERT_ID()),'{row[2]}');"

        # sql command is the combination of the 4 insert statements + begin and commit
        sqlcommand = begin + "\n" + userInsert + emailInsert + "\n"  + phoneInsert  + "\n" + usernameInsert + "\n" + commit
        inserts.append(sqlcommand)


# write the sql commands to a file
with open("final_insert_statements.sql", "w") as file:
    for insert in inserts:
        file.write(insert + "\n")







