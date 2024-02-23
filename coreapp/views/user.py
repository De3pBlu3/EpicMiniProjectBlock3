from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from coreapp.views.decorators import user_login_required
from coreapp import utils
from .auth import validate_details

@user_login_required
def home(request):
    user = request.session["user"]
    
    if user["type"] == 1:
        # Redirect to coordinator view
        return redirect("/coordinator/home")
    elif user["type"] == 2:
        # ... or admin home, as appropriate
        return redirect("/admin")
    
    with connection.cursor() as cursor:
        # What events are running, and is the user signed up for any of them?
        cursor.execute("""
            SELECT
                events.id,
                events.club_id,
                title,
                description,
                event_start,
                event_end,
                venue_id,
                venue,
                ea.approved IS NOT NULL as user_has_applied,
                ea.approved as user_application_status
            FROM events
            JOIN venues on events.venue_id = venues.id
            LEFT JOIN event_attendance_applications ea ON events.id = ea.event_id and ea.user_id=%s;
        """, [user["id"]])
        
        event_data = utils.fetchall_dict(cursor)

    return render(request, "pages/user/home.html", {
        "events": event_data
    })

@user_login_required
def update_user(request):
    user = request.session["user"]
    if user is None:
        return redirect('/login')

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT users.type, users.password_hash, users.address, user_emails.email, user_usernames.username, user_phones.phone 
            FROM users
            JOIN user_phones ON users.id = user_phones.user_id
            JOIN user_emails ON users.id = user_emails.user_id
            JOIN user_usernames ON users.id = user_usernames.user_id
            WHERE users.id = %s;
        """, [user["id"]])
        user_data = utils.fetchall_dict(cursor)[0]
    print(user_data)
    return render(request, 'pages/user/details.html', {'user_data': user_data})

@user_login_required
@require_http_methods(["POST"])
def update_attempt(request):
    error, details = validate_details(request.POST)
    if error is not None:
        return render(request, "pages/user/details.html", {
            "toast": {
                "text": error,
                "type": "danger"
            }
        })
    
    else:
        user_id = request.session["user"]["id"]
        insert_updated_user(user_id, details)

def insert_updated_user(user_id, info):
    with connection.cursor() as cursor:
        type, hashed_password, address, username, email, phonenumber = info

        cursor.execute("UPDATE users SET type=%s, password_hash=%s, address=%s WHERE users.id=%s", [type, hashed_password, address, user_id])
        cursor.execute("UPDATE user_phones SET phone=%s WHERE user_id=%s", [phonenumber, user_id])
        cursor.execute("UPDATE user_emails SET email=%s WHERE user_id=%s", [email, user_id])
        cursor.execute("UPDATE user_usernames SET username=%s WHERE user_id=%s", [username, user_id])

@require_http_methods(["POST"])
@user_login_required
def add_event_application(request):
    user_id = request.session["user"]["id"]
    event_id = request.POST.get("event_id")
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT(*) FROM event_attendance_applications WHERE user_id=%s AND event_id=%s", [user_id, event_id])
        count = cursor.fetchone()[0]
        
    if count == 0:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO event_attendance_applications(user_id, event_id, approved) VALUES(%s, %s, FALSE)", [user_id, event_id])
    return redirect('/home')

