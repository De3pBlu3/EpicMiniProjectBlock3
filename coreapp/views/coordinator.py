from django.db import connection
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods
from coreapp.views.decorators import coordinator_login_required
from coreapp import utils

@coordinator_login_required
def home(request):
    user = request.session["user"]
        
    with connection.cursor() as cursor:
        # What club is this coordinator part of?
        cursor.execute("""
            SELECT id, description, approved
            FROM clubs
            WHERE coordinator=%s;
        """, [user["id"]])
        
    
        ret = utils.fetchall_dict(cursor)
        club = ret[0] if len(ret) != 0 else None
        
        if club is None:
            return redirect("/coordinator/clubcreation")

        if not club["approved"]:
            return render(request, "pages/coordinator/pendingapproval.html")
            
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
    
@coordinator_login_required
def create_club(request):    
    return render(request, "pages/coordinator/clubcreation.html")

@coordinator_login_required
@require_http_methods(["POST"])
def club_creation_attempt(request):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO clubs(description, coordinator) VALUES (%s, %s)", [request.POST["club-description"], request.session["user"]["id"]])
        cursor.execute("INSERT INTO club_applications(club_id) VALUES ((SELECT id FROM clubs WHERE last_insert_rowid() == clubs.ROWID))")

    return redirect("/coordinator/home")