from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from coreapp.views.decorators import user_login_required
from coreapp import utils

@user_login_required
def home(request):
    user = request.session["user"]
    
    if user["type"] == 1:
        # Redirect to coordinator view
        return redirect("/coordinator/home")
    elif user["type"] == 2:
        # ... or admin home, as appropriate
        return redirect("/admin/home")
    
    with connection.cursor() as cursor:
        # What events are running, and is the user signed up for any of them?
        cursor.execute("""
            SELECT
                events.id,
                events.club_id,
                event_start,
                event_end,
                venue_id,
                venue,
                ea.approved IS NOT NULL as user_has_applied,
                ea.approved as user_application_status
            FROM events
            JOIN venues on events.venue_id = venues.id
            LEFT JOIN event_applications ea ON events.id = ea.event_id and ea.user_id=%s;
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
            SELECT users.address, user_emails.email, user_usernames.username, user_phones.phone 
            FROM users
            JOIN user_phones ON users.id = user_phones.user_id
            JOIN user_emails ON users.id = user_emails.user_id
            JOIN user_usernames ON users.id = user_usernames.user_id
            WHERE users.id = %s;
        """, [user["id"]])
        user_data = utils.fetchall_dict(cursor)[0]
    print(user_data)
    return render(request, 'pages/user/details.html', {'user_data': user_data})