from django.db import connection
from django.http import HttpResponse
from django.shortcuts import render
from coreapp.views.decorators import coordinator_login_required
from coreapp import utils

@coordinator_login_required
def home(request):
    user = request.session["user"]
        
    with connection.cursor() as cursor:
        # What club is this coordinator part of?
        cursor.execute("""
            SELECT id, description
            FROM clubs
            WHERE coordinator=%s;
        """, [user["id"]])
        
    
        ret = utils.fetchall_dict(cursor)
        club = ret[0] if len(ret) != 0 else None
        if club is None:
            return HttpResponse("TODO: redirect to club creation page")

        # What events is this club running right now?
        cursor.execute("""
            SELECT
                events.id, 
                event_start,
                event_end,
                COUNT(ea.user_id) as num_requested_attendees
            FROM events
            LEFT JOIN event_applications ea ON ea.event_id=events.id
            WHERE events.club_id=%s
            GROUP BY events.id
        """, [club["id"]])

        event_data = utils.fetchall_dict(cursor)

    return render(request, "pages/coordinator/home.html", {
        "events": event_data
    })