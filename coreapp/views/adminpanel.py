from django.shortcuts import render, redirect
from coreapp.models import user_model
from coreapp.forms import ChangeApprovalForm, deregisterForm
from django.db import connection


# will change the approved status of a user, and the pending status, will not delete the user
def deregister(request):
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
                    """UPDATE users SET approved = 0, pending = 1 WHERE users.id = (select user_id from user_usernames where username = %s);""",
                    [username])
                cursor.execute(
                    """UPDATE user_applications SET approved = 0, pending = 1 WHERE user_applications.user_id = (select user_id from user_usernames where username = %s);""",
                    [username])

            return redirect('/admin')
        else:
            print("FORM IS INVALID")
            print(form.errors.as_data())
    return redirect('/admin')


# will change the pending status of a user, and the approved status, this WILL delete the user
def change_approval(request):
    print("CHANGE APPROVAL")
    if request.method == 'POST':
        form = ChangeApprovalForm(request.POST)
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
                        """UPDATE users SET approved = 1, pending = 0 WHERE users.id = (select user_id from user_usernames where username = %s);""",
                        [username])
                    cursor.execute(
                        """UPDATE user_applications SET approved = 1, pending = 0 WHERE user_applications.user_id = (select user_id from user_usernames where username = %s);""",
                        [username])
                else:
                    cursor.execute(
                        """UPDATE users SET approved = 0, pending = 0 WHERE users.id = (select user_id from user_usernames where username = %s);""",
                        [username])
                    cursor.execute(
                        """UPDATE user_applications SET approved = 0, pending = 0 WHERE user_applications.user_id = (select user_id from user_usernames where username = %s);""",
                        [username])
            return redirect('/admin')

    return redirect('/admin')


def all_user_admin(request):
    # If user.session_type != 0:
    #    return render(request, 'error.html', {'error': "You are not an admin!"})
    #  or something akin to this i assume?

    change_approval_form = ChangeApprovalForm()
    deregister_form = deregisterForm(auto_id="register_%s")

    # TODO there may be a way to use views  for this, it seems silly to do two similar queries
    all_users = user_model.objects.raw("""
select users.id, username, type, email, address, phone, users.approved from users
inner join user_emails on users.id = user_emails.user_id
inner join user_phones on users.id = user_phones.user_id
inner join user_usernames on users.id = user_usernames.user_id where users.type = 0;""")

    pending_users = user_model.objects.raw("""
    select users.id, username, type, email, address, phone, users.approved from users
inner join user_emails on users.id = user_emails.user_id
inner join user_phones on users.id = user_phones.user_id
inner join user_usernames on users.id = user_usernames.user_id
WHERE users.approved = 0 AND users.pending = 1 and users.type = 0;""")

    coordinators = user_model.objects.raw("""
    select users.id, username, type, email, address, phone, users.approved from users
    inner join user_emails on users.id = user_emails.user_id
    inner join user_phones on users.id = user_phones.user_id
    inner join user_usernames on users.id = user_usernames.user_id
    WHERE users.approved = 1 AND users.pending = 0 AND users.type = 1;""")

    pending_coordinators = user_model.objects.raw("""
    select users.id, username, type, email, address, phone, users.approved from users
inner join user_emails on users.id = user_emails.user_id
inner join user_phones on users.id = user_phones.user_id
inner join user_usernames on users.id = user_usernames.user_id
WHERE users.approved = 0 AND users.pending = 1 AND users.type = 1;""")

    return render(request, 'admin.html', {'all_user_data': all_users,
                                          "pending_user_data": pending_users,
                                          "pending_coordinator_data": pending_coordinators,
                                          "all_coordinators_data": coordinators,
                                          "change_approval_form": change_approval_form,
                                          "deregister_form": deregister_form})
