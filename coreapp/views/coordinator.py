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
            JOIN club_applications ON clubs.id=club_applications.club_id
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
                title,
                description,
                events.id,
                event_start,
                event_end,
                COUNT(ea.user_id) as num_requested_attendees
            FROM events
            LEFT JOIN event_attendance_applications ea ON ea.event_id=events.id
            WHERE events.club_id=%s
            GROUP BY events.id
        """, [club["id"]])

        event_data = utils.fetchall_dict(cursor)

    return render(request, "pages/coordinator/home.html", {
        "events": event_data,
        "user_type": user["type"]
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

        cursor.execute(
            "INSERT INTO club_names(club_id, name) VALUES ((SELECT id FROM clubs WHERE last_insert_rowid() == clubs.ROWID), %s)", [request.POST["club-name"]])

        cursor.execute(
            "INSERT INTO club_applications(club_id) VALUES ((SELECT id FROM clubs WHERE last_insert_rowid() == clubs.ROWID))")

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
                INSERT INTO events (club_id, title, description, event_start, event_end, venue_id) 
                VALUES (%s, %s, %s, %s, %s, %s)""",
                [club["id"], request.POST["title"], request.POST["description"], request.POST["start-date"], request.POST["end-date"], venue_id])
    
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

@coordinator_login_required
def venue_creation(request):
    return render(request, "pages/coordinator/venuecreation.html", {"user_type": request.session["user"]["type"]})

@require_http_methods(["POST"])
@coordinator_login_required
def venue_creation_attempt(request):
    user_id = request.session["user"]["id"]
    with connection.cursor() as cursor:
        cursor.execute ('SELECT id FROM clubs WHERE coordinator=%s', [user_id])
        club_id = cursor.fetchone()[0]
    venue = request.POST.get("venue")
    
    # if field(s) is empty
    if not (venue and user_id and club_id):
        return HttpResponse("Input required")
    
    # if venue already exists 
    if check_venue_exists(venue):
        return HttpResponse("Venue Already exists")
    
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO venues (club_id, venue) VALUES (%s, %s)", [club_id, venue])

    # maybe return a success message? 
    return redirect("/coordinator/home")
