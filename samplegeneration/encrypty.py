import bcrypt
import csv


def encrypt_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(rounds=12)).decode("utf-8")


dbSQL = """insert into users (username, type, password_hash, address, registered) values ('admin', 2, 'secureAdminPass12!', 'Admin Central, Adminland', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ahoopper1', 0, 'iG8.C3!?+0%l', '094 Debra Trail', TRUE);
insert into users (username, type, password_hash, address, registered) values ('apetkov2', 0, 'hR4%HK0fGEhLpk+', '078 Grayhawk Pass', TRUE);
insert into users (username, type, password_hash, address, registered) values ('abremen3', 0, 'xU3+V2r=WM$H(F', '8201 Clarendon Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jhandscomb4', 0, 'uT1@VtZ{', '649 Hallows Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('fflarity5', 0, 'qS2@RfHD?QoN', '387 Express Place', TRUE);
insert into users (username, type, password_hash, address, registered) values ('sodoherty6', 0, 'pM1!)xaB+RKU`', '5 Florence Road', TRUE);
insert into users (username, type, password_hash, address, registered) values ('laskin7', 0, 'iC1"lmK7', '5 Village Green Drive', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jswaddle8', 0, 'lP1!P"N>x', '33563 Quincy Place', TRUE);
insert into users (username, type, password_hash, address, registered) values ('cmackettrick9', 0, 'mA3&>,NNuy', '30690 Meadow Ridge Trail', TRUE);
insert into users (username, type, password_hash, address, registered) values ('nllewellyna', 0, 'xE4/xy#x{N', '6937 Buhler Circle', TRUE);
insert into users (username, type, password_hash, address, registered) values ('npriddleb', 0, 'vM6_eVbl8Al', '55 Stang Pass', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mcamplinc', 0, 'gF6&z.!)', '47683 Hansons Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('dberreyd', 0, 'oA5}smqr}+S@S0W', '67 Sunbrook Junction', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mcrichmere', 0, 'sO2$$~e!<@Ol?zku', '4417 Autumn Leaf Circle', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bgonzalvof', 0, 'iQ9+bpdi_\`RvzhI', '6841 Forster Terrace', TRUE);
insert into users (username, type, password_hash, address, registered) values ('gaugusteg', 0, 'sM3@B@Fd`e9', '23 Victoria Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mwinsparh', 0, 'hA2=ntf~V2S!2', '13132 Karstens Pass', TRUE);
insert into users (username, type, password_hash, address, registered) values ('reweri', 0, 'lS5=p\hAfq', '7 Eagan Point', TRUE);
insert into users (username, type, password_hash, address, registered) values ('cryhorovichj', 0, 'wE2/ny,5S', '5187 Dwight Trail', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jdouglask', 0, 'tX0)CX%{Qk+H15Qu', '7949 Westend Crossing', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ybolmannl', 0, 'fD2&/@HH2', '06376 Roth Street', TRUE);
insert into users (username, type, password_hash, address, registered) values ('hputtockm', 0, 'aB4=M5*DJW,', '5 Holmberg Street', TRUE);
insert into users (username, type, password_hash, address, registered) values ('dwakelingn', 0, 'eE8+w{NXJAaM9', '2202 Kings Crossing', TRUE);
insert into users (username, type, password_hash, address, registered) values ('apetrovskyo', 0, 'mM9_I@_`o', '60939 Mifflin Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('nemorp', 0, 'mG6$i)T+DU\(uX', '71216 Fulton Park', TRUE);
insert into users (username, type, password_hash, address, registered) values ('scalderonq', 0, 'mL5@=#Mla', '078 Loomis Parkway', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ckirtlanr', 0, 'nK1<&Z)1%s$y$', '46 John Wall Drive', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bblevins', 0, 'uW3\6|Uu3+O2/%', '3099 Montana Crossing', TRUE);
insert into users (username, type, password_hash, address, registered) values ('thallgalleyt', 0, 'sG3!K@%E', '9 Sundown Plaza', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jschaumakeru', 0, 'cJ5!#Llp7', '13 6th Center', TRUE);
insert into users (username, type, password_hash, address, registered) values ('wmoodiev', 0, 'dL9>|16b9g}!', '86 Bellgrove Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bjugginsw', 0, 'jO7\RuTlOr5vw', '894 Onsgard Place', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mpeplerx', 0, 'pQ0(M8eS+', '872 Esch Center', TRUE);
insert into users (username, type, password_hash, address, registered) values ('krolfoy', 0, 'fK6/=Mu$q', '25 Fulton Plaza', TRUE);
insert into users (username, type, password_hash, address, registered) values ('cweeksz', 0, 'mC9>VkON\', '61 Caliangt Point', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bschmidt10', 0, 'dQ5=+9{fz3eTS', '9989 6th Crossing', TRUE);
insert into users (username, type, password_hash, address, registered) values ('abecerro11', 0, 'zJ1@l!Tf$5', '29 Derek Road', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jdive12', 0, 'fT1~c&Or', '555 Morningstar Terrace', TRUE);
insert into users (username, type, password_hash, address, registered) values ('fansill13', 0, 'hW9(Rd8u<RMuxJY', '25 Prentice Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('iheake14', 0, 'cP5,>\3?0%IW', '05 Kim Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bgriffen15', 0, 'yG9_Zbv%V', '656 Elmside Circle', TRUE);
insert into users (username, type, password_hash, address, registered) values ('dtite16', 0, 'uV1$Jt_b~ISL=', '01 Rieder Parkway', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mbizley17', 0, 'vR4@*G$,ZHZ(SHtx', '4743 Mcbride Place', TRUE);
insert into users (username, type, password_hash, address, registered) values ('nduce18', 0, 'hG6@bY"Y>foQ9c', '556 Scoville Center', TRUE);
insert into users (username, type, password_hash, address, registered) values ('everrick19', 0, 'aB2/BBUhq!''', '506 Debs Road', TRUE);
insert into users (username, type, password_hash, address, registered) values ('avanyukhin1a', 0, 'qJ1"E+8p4', '0757 Valley Edge Crossing', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bhankard1b', 0, 'iU9#FvG>)U#!9d$', '72291 Coleman Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('kcranage1c', 0, 'bY1`V_1Cz9S/', '390 Jackson Way', TRUE);
insert into users (username, type, password_hash, address, registered) values ('dhinckes1d', 0, 'cP3,nYA97', '01 Macpherson Park', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jtows1e', 0, 'sR7<%by1', '17 Bartelt Road', TRUE);
insert into users (username, type, password_hash, address, registered) values ('tswane1f', 0, 'rH0(W&/3CSxmw!_', '06935 Maryland Road', TRUE);
insert into users (username, type, password_hash, address, registered) values ('joldacre1g', 0, 'sQ5?XV|~GIG{wT', '9 Dayton Crossing', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mterese1h', 0, 'xQ1+@1/8b}W6', '912 Stone Corner Point', TRUE);
insert into users (username, type, password_hash, address, registered) values ('amcgorley1i', 0, 'iK2)H|Y\D', '0759 West Circle', TRUE);
insert into users (username, type, password_hash, address, registered) values ('zraybould1j', 0, 'sE5/Y9)rx*V', '52 Elgar Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('gcolomb1k', 0, 'wC2=,<7B,!>n6', '26785 Eliot Lane', TRUE);
insert into users (username, type, password_hash, address, registered) values ('fsivyer1l', 0, 'uI7>8lxup@aC(Xg', '65 Killdeer Road', TRUE);
insert into users (username, type, password_hash, address, registered) values ('lbytheway1m', 0, 'yQ8\+!R?#jHW*.', '39 Ramsey Place', TRUE);
insert into users (username, type, password_hash, address, registered) values ('calessandone1n', 0, 'qD5)X~xOZ', '509 Garrison Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('fkunkler1o', 0, 'eE4${gsDQZ1', '57 Forest Parkway', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bbortolomei1p', 0, 'lY4_.}<\Z.', '0 Crownhardt Pass', TRUE);
insert into users (username, type, password_hash, address, registered) values ('torrin1q', 0, 'rT6/DH,K!3@.', '963 Manufacturers Street', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mromanet1r', 0, 'bJ4<2qjv4/17', '64881 Truax Place', TRUE);
insert into users (username, type, password_hash, address, registered) values ('pgreatrex1s', 0, 'qJ2@_psY>', '166 Hallows Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bmainds1t', 0, 'hH8&4{0SZ48', '690 Spenser Center', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ctop1u', 0, 'kH5$ttiR', '11523 Tony Junction', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ihowis1v', 0, 'yJ8@C=X/Mvqf/vY', '1089 Nelson Pass', TRUE);
insert into users (username, type, password_hash, address, registered) values ('adownham1w', 0, 'cB4(E}Wsk0H!0l', '432 8th Alley', TRUE);
insert into users (username, type, password_hash, address, registered) values ('dnurcombe1x', 0, 'lF7}iK`u}MF/h)', '70 David Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ctowers1y', 0, 'xD6@NPL1&8J2|', '2 Bartelt Pass', TRUE);
insert into users (username, type, password_hash, address, registered) values ('kaldrich1z', 0, 'qL0,SxkFR', '0094 Thompson Plaza', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mschubart20', 0, 'uW8"Gwl48V9(T@q%', '88 Monument Lane', TRUE);
insert into users (username, type, password_hash, address, registered) values ('tseine21', 0, 'nQ8$lgA<mS}pb', '9174 Kipling Junction', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ttrousdell22', 0, 'sH3!6k/UHBoz5\c', '6 Almo Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jvayne23', 0, 'lX9`EcUvQjm', '349 Monument Court', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mdavio24', 0, 'eC4>R}X/9u', '76 Northland Terrace', TRUE);
insert into users (username, type, password_hash, address, registered) values ('tnund25', 0, 'zI0#2E_.k~', '17596 Schmedeman Terrace', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mgalle26', 0, 'wV0{K+*1B"', '81 Oakridge Terrace', TRUE);
insert into users (username, type, password_hash, address, registered) values ('rdeverson27', 0, 'xF1%`jj}rn', '763 Sloan Circle', TRUE);
insert into users (username, type, password_hash, address, registered) values ('hologan28', 0, 'hY8~KTp&Q!9.', '3 Annamark Parkway', TRUE);
insert into users (username, type, password_hash, address, registered) values ('cjeenes29', 0, 'tA2?oo5rook', '77725 Graedel Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('lberens2a', 0, 'tP0$3SR7', '199 Oneill Plaza', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bhortop2b', 0, 'dL6.*/s@ZAq', '5 Forest Lane', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ceastby2c', 0, 'bS3,>17.', '0232 Garrison Park', TRUE);
insert into users (username, type, password_hash, address, registered) values ('qbenezeit2d', 0, 'gW6*n{kZsbX<L', '2280 Coolidge Terrace', TRUE);
insert into users (username, type, password_hash, address, registered) values ('akellen2e', 0, 'fR8#~FN%||92o', '65220 Everett Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('cdublin2f', 0, 'bB6{3|.,sF%', '82 Montana Trail', TRUE);
insert into users (username, type, password_hash, address, registered) values ('rsoar2g', 0, 'jA1@~ESyE', '50174 Haas Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('sflintoffe2h', 0, 'eQ3%}W~?d3e+zhj\', '3 Iowa Park', TRUE);
insert into users (username, type, password_hash, address, registered) values ('rrushford2i', 0, 'pL6@PH`"n*Uz*', '598 Oneill Lane', TRUE);
insert into users (username, type, password_hash, address, registered) values ('snewlin2j', 0, 'iU3"N@kv`{/N_m+}', '8 Ilene Center', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ddopson2k', 0, 'hC7}QhS!', '90 Swallow Way', TRUE);
insert into users (username, type, password_hash, address, registered) values ('bserman2l', 0, 'lK5?EB)_1>', '65 Texas Alley', TRUE);
insert into users (username, type, password_hash, address, registered) values ('tkenwrick2m', 0, 'kV5)qo1JO', '485 Coleman Terrace', TRUE);
insert into users (username, type, password_hash, address, registered) values ('kcoggon2n', 0, 'bV6(<~_qR', '86 Sunfield Crossing', TRUE);
insert into users (username, type, password_hash, address, registered) values ('efresson2o', 0, 'iU7=hu79ff,5y', '8 Rieder Plaza', TRUE);
insert into users (username, type, password_hash, address, registered) values ('lconnor2p', 0, 'fE7@th.M3.UeoI', '80714 Springs Way', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jlambkin2q', 0, 'cO6`OXw3p', '131 Trailsway Center', TRUE);
insert into users (username, type, password_hash, address, registered) values ('pphillipson2r', 0, 'bI8#SZ7Yj,', '150 Hudson Drive', TRUE);
insert into users (username, type, password_hash, address, registered) values ('eivanyushin2s', 0, 'qK3`<+p=', '9150 Ruskin Park', TRUE);
insert into users (username, type, password_hash, address, registered) values ('rdurban2t', 0, 'qQ8?E=_$Em\i7', '40 Ronald Regan Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ptiffney2u', 0, 'mD6"@b6n,"G%t', '0 East Trail', TRUE);
insert into users (username, type, password_hash, address, registered) values ('rkynnd2v', 0, 'iM0\.RlkNTU', '5879 West Plaza', TRUE);
insert into users (username, type, password_hash, address, registered) values ('wtither2w', 0, 'dA1&n6mkhPrWeA<g', '68230 Sloan Circle', TRUE);
insert into users (username, type, password_hash, address, registered) values ('rscorah2x', 0, 'iB7@I2`,X)qSNVS=', '6487 Cambridge Court', TRUE);
insert into users (username, type, password_hash, address, registered) values ('cnowland2y', 0, 'tC1_pfn.EOQ', '89 Waywood Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('gmcivor2z', 0, 'nC6\k,C{hR#', '6 Debs Alley', TRUE);
insert into users (username, type, password_hash, address, registered) values ('vbibb30', 0, 'kC4$2Q%M(>J', '452 Kingsford Court', TRUE);
insert into users (username, type, password_hash, address, registered) values ('clamperd31', 0, 'qQ3\,El<,QzF\', '9931 Veith Park', TRUE);
insert into users (username, type, password_hash, address, registered) values ('cpigford32', 0, 'dT2!57{>Up~)', '33 Norway Maple Plaza', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mbetham33', 0, 'aA0,i@jL9', '90 Burrows Way', TRUE);
insert into users (username, type, password_hash, address, registered) values ('fcrilly34', 0, 'vT3*fqBo#', '4188 Birchwood Court', TRUE);
insert into users (username, type, password_hash, address, registered) values ('jphebey35', 0, 'vP1&"v9a<S(}&T%', '718 Texas Street', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mkearley36', 0, 'dI8&6~hN`zY#X?@', '6229 Lunder Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('dkieran37', 0, 'bF2$g@?~mcd', '3011 Bellgrove Crossing', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mcorps38', 0, 'jA0,A2Bp>Sj', '4382 Bluestem Street', TRUE);
insert into users (username, type, password_hash, address, registered) values ('kslimming39', 0, 'wP7&f=#Yx~Ffv', '76 Mitchell Avenue', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ngouch3a', 0, 'oI3@`H1|w8py|', '41 Hayes Trail', TRUE);
insert into users (username, type, password_hash, address, registered) values ('dlimbourne3b', 0, 'qV4/zjhYXue>ag', '6904 Logan Hill', TRUE);
insert into users (username, type, password_hash, address, registered) values ('ualessandrelli3c', 0, 'nX0=xS4cW', '7933 Bashford Way', TRUE);
insert into users (username, type, password_hash, address, registered) values ('gparsall3d', 0, 'oQ9!wA}dg,+*<', '0839 Dexter Lane', TRUE);
insert into users (username, type, password_hash, address, registered) values ('mjarrel3e', 0, 'iQ0@q@K0C!tI`RL', '977 Petterle Street', TRUE);
insert into users (username, type, password_hash, address, registered) values ('apabelik3f', 0, 'kT3+QlvAOuvVUP', '201 Lotheville Drive', TRUE);
insert into users (username, type, password_hash, address, registered) values ('anewbery3g', 0, 'iA2.uO@6Bz/fT#`"', '6 Thompson Road', TRUE);"""

# split the string into a list of strings
user_insert_statement = dbSQL.split("\n")

# split by the space
user_insert_statement = [x.split() for x in user_insert_statement]

# get the passwords
passwords = [x[11] for x in user_insert_statement if x]

# replace the password with the encrypted password
for x in range(len(passwords)):
    user_insert_statement[x][11] = f"'{encrypt_password(passwords[x][1:-2])}',"

# join the strings back together
user_insert_statement = [" ".join(x) for x in user_insert_statement]

# # write the strings to a file
# with open("encrypted_users.sql", "w") as file:
#     for insert in user_insert_statement:
#         file.write(insert + "\n")


# pathToSql = r"original_insert_statements.sql"

pathToCSV = r"MOCK_DATA.csv"

begin = "BEGIN;"
commit = "COMMIT;"

data = []

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
        if row == 0:
            continue

        # userInsert must look like this
        # insert into users(type, password_hash, address, approved) values (2, 'PASS', 'Adminland', TRUE);
        userInsert = user_insert_statement[index - 1]

        # split the string into a list of strings
        user_insert_parts = userInsert.split()

        # get and store the username
        username = user_insert_parts[9][1:-2]  # remove the quotes

        # remove 'username,' from the fields and its value from the values
        del user_insert_parts[3]  # remove 'username,'
        del user_insert_parts[8]  # remove username value

        # join the strings back together
        userInsert = " ".join(user_insert_parts)

        # replace 'registered' with 'approved'
        userInsert = userInsert.replace('registered', 'approved')

        # create the insert statements
        emailInsert = f"INSERT INTO user_emails (user_id, email) VALUES((SELECT last_insert_rowid()),'{row[0]}');"
        phoneInsert = f"INSERT INTO user_phones (user_id, phone) VALUES((SELECT last_insert_rowid()),'{row[1]}');"
        usernameInsert = f"INSERT INTO user_usernames (user_id, username) VALUES((SELECT last_insert_rowid()),{username}');"

        # sql command is the combination of the 4 insert statements + begin and commit
        sqlcommand = begin + "\n" + userInsert + "\n" + emailInsert + "\n" + phoneInsert + "\n" + usernameInsert + "\n" + commit
        inserts.append(sqlcommand)

# write the sql commands to a file
with open("final_insert_statements.sql", "w") as file:
    for insert in inserts:
        file.write(insert + "\n")
