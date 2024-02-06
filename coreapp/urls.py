from django.urls import path

from .views import home, auth

urlpatterns = [
    path('', home.index),
    path('home', home.home),

    path('dummy_login', auth.dummy_login),
    path('login', auth.login),
    path('loginattempt', auth.loginattempt)
]