import re
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
from django.db import connection
import bcrypt

@require_http_methods(["GET"])
def login(request):
    return render(request, "login.html")

@require_http_methods(["POST"])
def loginattempt(request):
    # TODO: Login auth
    username = request.POST.get("username")
    password = request.POST.get("password")

    ## TODO check credentials
    if check_credentials(username, password):
        return HttpResponse("Success, routing to homepage!")
    else:
        return HttpResponse("Failed!")

@require_http_methods(["POST"])
def signupattempt(request):
    details = validate_details(request.POST)
    if details == False:
        return HttpResponse("You have invalid details. Please try again!")
    else:
        insert_user(details)
    return HttpResponse("You have registered please log in!")

def check_credentials(username, password):
    with connection.cursor() as cursor:
        cursor.execute("SELECT password_hash FROM users WHERE username=%s", (username,))
        stored = cursor.fetchone()

        if stored:
            print(stored)
            if bcrypt.checkpw(password.encode('utf-8'), stored[0]):
                return True
    return False

def insert_user(info):
    
    with connection.cursor() as cursor:
        sql1 = "INSERT INTO users(username, type, password_hash, address, registered) VALUES (%s, %s, %s, %s, 'false')"
        cursor.execute(sql1, info)

        # sql2 = "INSERT INTO user_email(user_id, email) VALUES ()"
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
        # TODO have a popup saying password is invalid 
        return False
    
    if not is_valid_password(password):
        # TODO have a popup saying username is invalid 
        return False
    
    hashed_password = bcrypt.hashpw(dict.get("password").encode('utf-8'), bcrypt.gensalt(rounds=12))
    if dict.get("user_type") == "user":
        type = 0
    elif dict.get("user_type") == "coordinator":
        type = 1
    else:
        return False
    email = dict.get("email")
    phonenumber = dict.get("phonenumber")
    address = dict.get("address")

    if email == '' or phonenumber == '' or address == ' ':
        return False 

    return (username, type, hashed_password, address)

