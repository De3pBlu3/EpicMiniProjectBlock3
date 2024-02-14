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
                    cursor.execute("UPDATE users SET approved = 1, pending = 0 WHERE users.id = (select user_id from user_usernames where username = %s)", [username])
                else:
                    cursor.execute("UPDATE users SET approved = 0, pending = 1 WHERE users.id = (select user_id from user_usernames where username = %s)", [username])
                    #todo create an sql trigger to delete the user when invalid?
            return redirect('/admin')

    form = userAlterForm()
    data = user_model.objects.raw("SELECT * FROM users")
    data2 = user_model.objects.raw("SELECT * FROM users WHERE registered = 0")
    # change username to be first 3 letters of username
    for person in data:
        person.password_hash = str(person.password_hash)[7:7+4] + "..."
    return render(request, 'admin.html', {'all_user_data': data, "pending_user_data": data2, "form": userAlterForm})

