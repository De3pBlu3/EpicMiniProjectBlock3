from django.shortcuts import redirect

def _check_user_or_redirect(func, condition_func, redirect_url="/login"):
    def inner(request, *args, **kwargs):
        if not "user" in request.session or not condition_func(request.session["user"]):
            return redirect(redirect_url)
        
        return func(request, *args, **kwargs)
    
    return inner
    

def user_login_required(func):
    return _check_user_or_redirect(func, lambda user: user['type'] == 0 or user['type'] == 1 or user['type'] == 2)

def coordinator_login_required(func):
    return _check_user_or_redirect(func, lambda user: user['type'] == 1 or user['type'] == 2)

def admin_login_required(func):
    return _check_user_or_redirect(func, lambda user: user['type'] == 2)