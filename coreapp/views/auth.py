from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render
import run_sql_script
from passlib.hash import bcrypt

@require_http_methods(["GET"])
def login(request):
    return render(request, "login.html")

@require_http_methods(["POST"])
def loginattempt(request):
    # TODO: Login auth
    username = request.POST.get("username")
    password = request.POST.get("password")
    hashed_password = bcrypt.hash(password)

    return redirect("/")
    print(run_sql_script())
    