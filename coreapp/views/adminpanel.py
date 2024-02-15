from django.shortcuts import render, redirect
from coreapp.models import user_model
from coreapp.forms import userAlterForm
from django.db import connection


def all_user_admin(request):
    # If user.session_type != 0:
    #    return render(request, 'error.html', {'error': "You are not an admin!"})
    #  or something akin to this i assume?

    if request.method == 'POST':
        form = userAlterForm(request.POST)
        print("RECIEVED POST")
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
                        "UPDATE users SET approved = 1, pending = 0 WHERE users.id = (select user_id from user_usernames where username = %s)",
                        [username])
                else:
                    cursor.execute(
                        "UPDATE users SET approved = 0, pending = 1 WHERE users.id = (select user_id from user_usernames where username = %s)",
                        [username])
                    # todo create an sql trigger to delete the user when invalid?
            return redirect('/admin')
    form = userAlterForm()  # else just unbound form

    # TODO there may be a way to use views for this, it seems silly to do two similar queries
    data = user_model.objects.raw("""
select users.id, username, type, email, address, phone, users.approved from users
inner join user_emails on users.id = user_emails.user_id
inner join user_phones on users.id = user_phones.user_id
inner join user_usernames on users.id = user_usernames.user_id""")

    data2 = user_model.objects.raw("""
    select users.id, username, type, email, address, phone, users.approved from users
inner join user_emails on users.id = user_emails.user_id
inner join user_phones on users.id = user_phones.user_id
inner join user_usernames on users.id = user_usernames.user_id
WHERE users.approved = 0 AND users.pending = 1""")

    return render(request, 'admin.html', {'all_user_data': data, "pending_user_data": data2, "form": userAlterForm})
