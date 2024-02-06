from django.urls import path

from .views import home, auth, adminpanel

urlpatterns = [
    path('', home.index),
    path('home', home.home),
    path('dummy_login', auth.dummy_login),
    path('login', auth.login),
    path('loginattempt', auth.loginattempt),
    path('admin', adminpanel.all_user_admin),
]