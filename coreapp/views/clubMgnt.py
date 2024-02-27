from django.shortcuts import render, redirect
from coreapp.forms import changeApprovalForm, deregisterForm, changeClubForm, changeEventAttendanceForm
from django.db import connection
from coreapp import utils
from coreapp.views.decorators import coordinator_login_required
from coreapp.views.coordinator import get_club


# will change the approved status of a user, and the pending status, will not delete the user
@coordinator_login_required
def user_deregister(request):
    # get club
    user = request.session["user"]
    club = get_club(user)

    if request.method == 'POST':
        form = deregisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']

            # change registered status
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE memberships SET approved = 0, pending = 1 WHERE memberships.user_id = (select user_id from user_usernames where username = %s) and memberships.club_id = %s;""",
                    [username, club["id"]])

            return redirect('/coordinator/clubmanagement')
    return redirect('/coordinator/clubmanagement')


@coordinator_login_required
def user_change_approval(request):
    # get club
    user = request.session["user"]
    club = get_club(user)
    if request.method == 'POST':
        form = changeApprovalForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            registered_value = form.cleaned_data['registered']

            # change registered status
            with connection.cursor() as cursor:
                if registered_value:
                    cursor.execute(
                        """UPDATE memberships SET approved = 1, pending = 0 WHERE memberships.user_id = (select user_id from user_usernames where username = %s) and memberships.club_id = %s;""",
                        [username, club["id"]])
                else:
                    cursor.execute(
                        """UPDATE memberships SET approved = 0, pending = 0 WHERE memberships.user_id = (select user_id from user_usernames where username = %s) and memberships.club_id = %s;""",
                        [username, club["id"]])

            return redirect('/coordinator/clubmanagement')

    return redirect('/coordinator/clubmanagement')


def event_attendance_change_approval(request):
    # get club
    user = request.session["user"]
    club = get_club(user)
    if request.method == 'POST':
        form = changeApprovalForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            registered_value = form.cleaned_data['registered']

            # change registered status
            with connection.cursor() as cursor:
                if registered_value:
                    cursor.execute(
                        """UPDATE event_attendance_applications SET approved = 1, pending = 0 WHERE event_attendance_applications.user_id = (select user_id from user_usernames where username = %s) and (select club_id from main.events where events.id = event_attendance_applications.event_id) = %s;""",
                        [username, club["id"]])
                else:
                    cursor.execute(
                        """UPDATE event_attendance_applications SET approved = 1, pending = 0 WHERE event_attendance_applications.user_id = (select user_id from user_usernames where username = %s) and (select club_id from main.events where events.id = event_attendance_applications.event_id) = %s;""",
                        [username, club["id"]])

            return redirect('/coordinator/clubmanagement')

    return redirect('/coordinator/clubmanagement')


def event_change_approval(request):
    # get club
    user = request.session["user"]
    club = get_club(user)
    if request.method == 'POST':
        form = changeApprovalForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            registered_value = form.cleaned_data['registered']

            # change registered status
            with connection.cursor() as cursor:
                if registered_value:
                    cursor.execute(
                        """UPDATE event_attendance_applications SET approved = 1, pending = 0 WHERE event_attendance_applications.user_id = (select user_id from user_usernames where username = %s) and (select club_id from main.events where events.id = event_attendance_applications.event_id) = %s;""",
                        [username, club["id"]])
                else:
                    cursor.execute(
                        """UPDATE event_attendance_applications SET approved = 1, pending = 0 WHERE event_attendance_applications.user_id = (select user_id from user_usernames where username = %s) and (select club_id from main.events where events.id = event_attendance_applications.event_id) = %s;""",
                        [username, club["id"]])

            return redirect('/coordinator/clubmanagement')

    return redirect('/coordinator/clubmanagement')


@coordinator_login_required
def coordinator_club_mgnt(request):
    change_approval_form = changeApprovalForm()
    deregister_form = deregisterForm(auto_id="register_%s")
    change_event_attendance_form = changeEventAttendanceForm(auto_id="event_attendance_%s")

    # get session - we can assume will be a coordinator
    user = request.session["user"]
    club = get_club(user)

    if club is None:
        return redirect("/coordinator/clubcreation")

    if not club["approved"]:
        return render(request, "pages/coordinator/pendingapproval.html")

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT users.id, username, type, email, address, phone, user_applications.approved 
            FROM users
            INNER JOIN user_emails ON users.id = user_emails.user_id
            INNER JOIN user_phones ON users.id = user_phones.user_id
            INNER JOIN user_usernames ON users.id = user_usernames.user_id
            INNER JOIN user_applications ON users.id = user_applications.user_id 
            inner join memberships on users.id = memberships.user_id
            WHERE memberships.club_id = %s and memberships.approved = 1 and memberships.pending = 0;
        """, [club["id"]])
        all_users = utils.fetchall_dict(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT users.id, username, type, email, address, phone, user_applications.approved 
            FROM users
            INNER JOIN user_emails ON users.id = user_emails.user_id
            INNER JOIN user_phones ON users.id = user_phones.user_id
            INNER JOIN user_usernames ON users.id = user_usernames.user_id
            INNER JOIN user_applications ON users.id = user_applications.user_id 
            inner join memberships on users.id = memberships.user_id
            WHERE memberships.club_id = %s and memberships.approved = 0 and memberships.pending = 1;
        """, [club["id"]])
        pending_users = utils.fetchall_dict(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
            select events.title, username from event_attendance_applications
            inner join events on event_attendance_applications.event_id = events.id
            inner join user_usernames on event_attendance_applications.user_id = user_usernames.user_id
            where approved = 1 and pending = 0 and events.club_id = %s;
        """, [club["id"]])
        attending_users = utils.fetchall_dict(cursor)

    attending_dict = {}
    for event in attending_users:
        if event["title"] in attending_dict:
            attending_dict[event["title"]].append(event["username"])
        else:
            attending_dict[event["title"]] = [event["username"]]

    with connection.cursor() as cursor:
        cursor.execute("""
            select events.title, username from event_attendance_applications
            inner join events on event_attendance_applications.event_id = events.id
            inner join user_usernames on event_attendance_applications.user_id = user_usernames.user_id
            where approved = 0 and pending = 1 and events.club_id = %s;
        """, [club["id"]])
        pending_attending_users = utils.fetchall_dict(cursor)

    pending_attending_dict = {}
    for event in pending_attending_users:
        if event["title"] in pending_attending_dict:
            pending_attending_dict[event["title"]].append(event["username"])
        else:
            pending_attending_dict[event["title"]] = [event["username"]]

    # combine all the data into one dict
    combined_dict = {}

    for event_title in set(attending_dict.keys()).union(pending_attending_dict.keys()):
        combined_dict[event_title] = {
            "attending": attending_dict.get(event_title, []),
            "pending": pending_attending_dict.get(event_title, [])
        }

    # todo might be cool to change pending/attending users into one single dict, means for loop and be written easier
    return render(request, 'pages/coordinator/clubmanagement.html', {'all_user_data': all_users,
                                                                     "pending_user_data": pending_users,
                                                                     "event_users": combined_dict,

                                                                     "change_approval_form": change_approval_form,
                                                                     "deregister_form": deregister_form,
                                                                     "change_attendance_form": change_event_attendance_form
                                                                     })
