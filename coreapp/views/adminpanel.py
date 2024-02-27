from django.shortcuts import render, redirect
from coreapp.forms import changeApprovalForm, deregisterForm, changeClubForm
from django.db import connection
from coreapp import utils
from coreapp.views.decorators import admin_login_required


# will change the approved status of a user, and the pending status, will not delete the user
@admin_login_required
def user_deregister(request):
    if request.method == 'POST':
        form = deregisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            
            # change registered status
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE user_applications SET approved = 0, pending = 1 WHERE user_applications.user_id = (select user_id from user_usernames where username = %s);""",
                    [username])

            return redirect('/admin')
    return redirect('/admin')


# will change the pending status of a user, and the approved status, this WILL delete the user
@admin_login_required
def user_change_approval(request):
    if request.method == 'POST':
        form = changeApprovalForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            registered_value = form.cleaned_data['registered']

            # change registered status
            with connection.cursor() as cursor:
                if registered_value:
                    cursor.execute(
                        """UPDATE user_applications SET approved = 1, pending = 0 WHERE user_applications.user_id = (select user_id from user_usernames where username = %s);""",
                        [username])
                else:
                    cursor.execute(
                        """UPDATE user_applications SET approved = 0, pending = 0 WHERE user_applications.user_id = (select user_id from user_usernames where username = %s);""",
                        [username])
            return redirect('/admin')

    return redirect('/admin')


@admin_login_required
def club_change_approval(request):
    if request.method == 'POST':
        form = changeClubForm(request.POST)
        if form.is_valid():
            club_id = form.cleaned_data['club_id']
            registered_value = form.cleaned_data['approved']

            # change registered status
            with connection.cursor() as cursor:
                if registered_value:
                    cursor.execute(
                        """UPDATE club_applications SET approved = 1, pending = 0 WHERE club_applications.club_id = %s;""",
                        [club_id])
                else:
                    cursor.execute(
                        """UPDATE club_applications SET approved = 0, pending = 0 WHERE club_applications.club_id = %s;""",
                        [club_id])
            return redirect('/admin')

    return redirect('/admin')


@admin_login_required
def all_user_admin(request):
    change_approval_form = changeApprovalForm()
    deregister_form = deregisterForm(auto_id="register_%s")
    club_change_approval_form = changeClubForm(auto_id="club_%s")

    # TODO there may be a way to use views  for this, it seems silly to do two similar queries
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM all_user_info WHERE type = 0")
        all_users = utils.fetchall_dict(cursor)
        
        cursor.execute("SELECT * FROM all_user_info WHERE approved = 0 AND pending = 1 AND type = 0")
        pending_users = utils.fetchall_dict(cursor)

        cursor.execute("SELECT * FROM all_user_info WHERE approved = 1 AND pending = 0 AND type = 1")
        coordinators = utils.fetchall_dict(cursor)

        cursor.execute("SELECT * FROM all_user_info WHERE approved = 0 AND pending = 1 AND type = 1")
        pending_coordinators = utils.fetchall_dict(cursor)

        cursor.execute("""
            SELECT * FROM all_club_info
            WHERE approved = 1 AND pending = 0
            ORDER BY id;
        """)
        clubs = utils.fetchall_dict(cursor)

        cursor.execute("""
            SELECT * FROM all_club_info
            WHERE approved = 0 AND pending = 1
            ORDER BY id;
            """)
        pending_clubs = utils.fetchall_dict(cursor)

        cursor.execute("""
            SELECT clubs.id, club_names.name, clubs.description, user_usernames.username
            FROM clubs
            INNER JOIN club_names on clubs.id = club_names.club_id
            INNER JOIN memberships ON clubs.id = memberships.club_id
            INNER JOIN user_usernames ON memberships.user_id = user_usernames.user_id
            ORDER BY clubs.id;
            """)

        all_memberships = utils.fetchall_dict(cursor)

    # split all_clubs into a dictionary of (club name, club_id) as key and list of users in each club as value
    club_dict = {}
    for club in all_memberships:
        key = (club["name"], club["id"])
        if key not in club_dict:
            club_dict[key] = []
        club_dict[key].append(club["username"])

    return render(request, 'admin.html', {'all_user_data': all_users,
                                          "pending_user_data": pending_users,
                                          "pending_coordinator_data": pending_coordinators,
                                          "all_coordinators_data": coordinators,
                                          "change_approval_form": change_approval_form,
                                          "deregister_form": deregister_form,
                                          "change_club_form": club_change_approval_form,
                                          "membership_requests": club_dict,
                                          "all_clubs": clubs,
                                          "pending_clubs": pending_clubs})
