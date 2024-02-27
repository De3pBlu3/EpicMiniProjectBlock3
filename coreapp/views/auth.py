import re
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from django.db import connection
import bcrypt

@require_http_methods(["GET"])
def login(request):
    return render(request, "pages/login.html")

@require_http_methods(["POST"])
def loginattempt(request):
    username = request.POST.get("username")
    password = request.POST.get("password")

    error, user = check_credentials(username, password)
    
    if error is None:
        request.session["user"] = user
        return redirect("/home")
    else:
        return render(request, "pages/login.html", {
            "toast": {
                "text": error,
                "type": "danger"
            }
        })

@require_http_methods(["POST"])
def signupattempt(request):
    error, details = validate_details(request.POST)
    if error is not None:
        return render(request, "pages/login.html", {
            "toast": {
                "text": error,
                "type": "danger"
            }
        })
    else:
        insert_user(details)
    
    return render(request, "pages/login.html", {
        "toast": {
            "text": "You have registered! Once the admin has approved you please log in.",
        }
    })

def check_credentials(username, password):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id, password_hash, approved, type
            FROM users
            JOIN user_usernames ON users.id=user_usernames.user_id
            JOIN user_applications ON users.id=user_applications.user_id
            WHERE user_usernames.username=%s
        """, (username,))
        
        stored = cursor.fetchone()

        if stored:
            id, hash, approved, type = stored
            if bcrypt.checkpw(password.encode('utf-8'), hash.encode("utf-8")):
                if approved:
                    return None, {
                        "type": type,
                        "username": username,
                        "id": id
                    } 
                else:
                    return "Please wait for your account to be approved by the administrator before logging in", None
            
    return "Error logging in!", None

def insert_user(info):
    with connection.cursor() as cursor:
        type, hashed_password, address, username, email, phonenumber = info    
        
        cursor.execute("INSERT INTO users(type, password_hash, address) VALUES (%s, %s, %s)", [type, hashed_password, address])
        
        cursor.execute("SELECT users.id from users where last_insert_rowid() == users.ROWID")
        user_id = cursor.fetchone()[0]
        
        cursor.execute("INSERT INTO user_applications(user_id) VALUES (%s)", [user_id])
        cursor.execute("INSERT INTO user_usernames(user_id, username) VALUES (%s, %s)", [user_id, username])
        cursor.execute("INSERT INTO user_emails(user_id, email) VALUES (%s, %s)", [user_id, email])
        cursor.execute("INSERT INTO user_phones(user_id, phone) VALUES (%s, %s)", [user_id, phonenumber])
    
        connection.commit()

def is_valid_username(username):
    pattern = r'^[a-zA-Z][a-zA-Z0-9._-]{0,18}$'
    return re.match(pattern, username) is not None

def is_valid_password(password):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z\d]).{8,}$'
    return re.match(pattern, password) is not None

def validate_details(dict):
    username = dict.get("username")
    password = dict.get("password")

    if not is_valid_username(username):
        return "Username is invalid", None
    
    if not is_valid_password(password):
        return "Password is invalid", None

    # added code to check if the username already exists
    with connection.cursor() as cursor:
        cursor.execute("SELECT EXISTS(SELECT 1 FROM user_usernames WHERE username=%s)", [username])
        exists = cursor.fetchone()[0]
        if exists:
            return "Username already exists", None
            
    hashed_password = bcrypt.hashpw(dict.get("password").encode('utf-8'), bcrypt.gensalt(rounds=12)).decode("utf-8")
    
    if dict.get("user_type") == "user":
        type = 0
    elif dict.get("user_type") == "coordinator":
        type = 1
    else:
        return "Invalid user type", None
    email = dict.get("email")
    phonenumber = dict.get("phonenumber")
    address = dict.get("address")

    if email == '' or phonenumber == '' or address == ' ':
        return "Email, phone number and address are all required", None

    return None, (type, hashed_password, address, username, email, phonenumber)

