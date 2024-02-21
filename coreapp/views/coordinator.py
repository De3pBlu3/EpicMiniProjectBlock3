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
            SELECT id, description
            FROM clubs
            WHERE coordinator=%s;
        """, [user["id"]])

        ret = utils.fetchall_dict(cursor)
        club = ret[0] if len(ret) != 0 else None

        if club is None:
            return redirect("/coordinator/clubcreation")

        # What events is this club running right now?
        cursor.execute("""
            SELECT
                events.id,
                event_end,
                COUNT(ea.user_id) as num_requested_attendees
            FROM events
            LEFT JOIN event_attendance_applications ea ON ea.event_id=events.id
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
        cursor.execute("INSERT INTO clubs(description, coordinator) VALUES (%s, %s)", [
                       request.POST["club-description"], request.session["user"]["id"]])

    return redirect("/coordinator/home")


@coordinator_login_required
def create_event(request):
    return render(request, "pages/coordinator/eventcreation.html")


@coordinator_login_required
@require_http_methods(["POST"])
def event_creation_attempt(request):
    user = request.session["user"]

    # assuming that each club has a coordinator
    # to get what club the coordinator is in
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id
            FROM clubs
            WHERE coordinator=%s;
        """, [user["id"]])

        club_data = utils.fetchall_dict(cursor)
        club = club_data[0]

    venue = request.POST["venue"]

    # check if venue exists
    if not (venue_id := check_venue_exists(venue)):
        return HttpResponse("Venue doesn't exists")
    
    # inserting into database
    with connection.cursor() as cursor:
        cursor.execute("""
                INSERT INTO events (club_id, event_start, event_end, venue_id) 
                VALUES (%s, %s, %s, %s)""",
                [club["id"], request.POST["start-date"], request.POST["end-date"], venue_id])
    
    # redirecting into home page
    return redirect("/coordinator/home")

def check_venue_exists(venue):
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT id
            FROM venues
            WHERE venue = %s
        """, [venue])
        result = cursor.fetchone()
        print(result)
        return result[0] if result else False


    
