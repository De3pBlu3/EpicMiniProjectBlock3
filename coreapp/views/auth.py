from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect, render

@require_http_methods(["GET"])
def dummy_login(request):
    request.session['user'] = {
        "id": 2,
        "username": "rdumphries1",
        "type": 0,
    }
    
    return redirect("/home")

@require_http_methods(["GET"])
def login(request):
    return render(request, "pages/login.html")

@require_http_methods(["POST"])
def loginattempt(request):
    # TODO: Login auth
    print (request.POST)
    
    return redirect("/")