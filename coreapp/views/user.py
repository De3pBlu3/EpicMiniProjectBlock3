from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect, render

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
        return redirect("/admin")
    
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