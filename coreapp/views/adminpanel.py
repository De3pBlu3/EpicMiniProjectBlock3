from django.shortcuts import render, redirect
from coreapp.models import user_model
from coreapp.forms import changeApprovalForm, deregisterForm, changeClubForm
from django.db import connection
from coreapp import utils
from coreapp.views.decorators import admin_login_required


# will change the approved status of a user, and the pending status, will not delete the user
@admin_login_required
def user_deregister(request):
    print("DEREGISTER")
    if request.method == 'POST':
        print("POST")
        form = deregisterForm(request.POST)
        if form.is_valid():
            print("FORM IS VALID")
            username = form.cleaned_data['username']

            print("FORM IS VALID")
            print(username)

            # change registered status
            with connection.cursor() as cursor:
                cursor.execute(
                    """UPDATE user_applications SET approved = 0, pending = 1 WHERE user_applications.user_id = (select user_id from user_usernames where username = %s);""",
                    [username])

            return redirect('/admin')
        else:
            print("FORM IS INVALID")
            print(form.errors.as_data())
    return redirect('/admin')


# will change the pending status of a user, and the approved status, this WILL delete the user
@admin_login_required
def user_change_approval(request):
    print("CHANGE APPROVAL")
    if request.method == 'POST':
        form = changeApprovalForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            registered_value = form.cleaned_data['registered']

            print("FORM IS VALID")
            print(username)
            print(registered_value)

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
    print("CHANGE APPROVAL")
    if request.method == 'POST':
        form = changeClubForm(request.POST)
        if form.is_valid():
            club_id = form.cleaned_data['club_id']
            registered_value = form.cleaned_data['approved']

            print("FORM IS VALID")
            print(club_id)
            print(registered_value)

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
        cursor.execute("""
            SELECT users.id, username, type, email, address, phone, user_applications.approved 
            FROM users
            INNER JOIN user_emails ON users.id = user_emails.user_id
            INNER JOIN user_phones ON users.id = user_phones.user_id
            INNER JOIN user_usernames ON users.id = user_usernames.user_id
            INNER JOIN user_applications ON users.id = user_applications.user_id 
            WHERE users.type = 0;
        """)
        all_users = utils.fetchall_dict(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT users.id, username, type, email, address, phone, user_applications.approved 
            FROM users
            INNER JOIN user_emails ON users.id = user_emails.user_id
            INNER JOIN user_phones ON users.id = user_phones.user_id
            INNER JOIN user_usernames ON users.id = user_usernames.user_id
            INNER JOIN user_applications ON users.id = user_applications.user_id
            WHERE user_applications.approved = 0 AND user_applications.pending = 1 AND users.type = 0;
        """)
        pending_users = utils.fetchall_dict(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT users.id, username, type, email, address, phone, user_applications.approved 
            FROM users
            INNER JOIN user_emails ON users.id = user_emails.user_id
            INNER JOIN user_phones ON users.id = user_phones.user_id
            INNER JOIN user_usernames ON users.id = user_usernames.user_id
            INNER JOIN user_applications ON users.id = user_applications.user_id
            WHERE user_applications.approved = 1 AND user_applications.pending = 0 AND users.type = 1;
        """)
        coordinators = utils.fetchall_dict(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT users.id, username, type, email, address, phone, user_applications.approved 
            FROM users
            INNER JOIN user_emails ON users.id = user_emails.user_id
            INNER JOIN user_phones ON users.id = user_phones.user_id
            INNER JOIN user_usernames ON users.id = user_usernames.user_id
            INNER JOIN user_applications ON users.id = user_applications.user_id
            WHERE user_applications.approved = 0 AND user_applications.pending = 1 AND users.type = 1;
        """)
        pending_coordinators = utils.fetchall_dict(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT clubs.id, clubs.description, club_names.name, user_usernames.username
            FROM clubs
            INNER JOIN club_names ON clubs.id = club_names.club_id
            INNER JOIN club_applications ON clubs.id = club_applications.club_id
            inner join user_usernames on clubs.coordinator = user_usernames.user_id
            WHERE club_applications.approved = 1 AND club_applications.pending = 0
            ORDER BY clubs.id;
        """)
        clubs = utils.fetchall_dict(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT clubs.id, clubs.description, club_names.name, user_usernames.username
            FROM clubs
            INNER JOIN club_names ON clubs.id = club_names.club_id
            INNER JOIN club_applications ON clubs.id = club_applications.club_id
            inner join user_usernames on clubs.coordinator = user_usernames.user_id
            WHERE club_applications.approved = 0 AND club_applications.pending = 1
            ORDER BY clubs.id;
            """)
        pending_clubs = utils.fetchall_dict(cursor)

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT clubs.id, club_names.name, clubs.description, user_usernames.username
            FROM clubs
            INNER JOIN club_names on clubs.id = club_names.club_id
            INNER JOIN memberships ON clubs.id = memberships.club_id
            INNER JOIN user_usernames ON memberships.user_id = user_usernames.user_id
            ORDER BY clubs.id;
            """)
        all_memberships = utils.fetchall_dict(cursor)

    # split all_clubs into a dictionary of clubs as key and list of users in each club as value
    club_dict = {}
    for club in all_memberships:
        if club["name"] not in club_dict:
            club_dict[club["name"]] = []
        club_dict[club["name"]].append(club["username"])

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
