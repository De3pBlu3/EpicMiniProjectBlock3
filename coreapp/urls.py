from django.urls import path

from .views import home, auth

urlpatterns = [
    path('', home.index),

    path('login', auth.login),
    path('loginattempt', auth.loginattempt)
]