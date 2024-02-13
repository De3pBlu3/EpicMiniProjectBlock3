from django.urls import path

from .views import index, auth, adminpanel, user, coordinator

urlpatterns = [
    path('', index.index),

    path('login', auth.login),
    path('loginattempt', auth.loginattempt),
    path('signupattempt', auth.signupattempt),
    
    path('admin', adminpanel.all_user_admin),
    
    path('home', user.home),
    
 
    path('coordinator/home', coordinator.home),
    path('coordinator/clubcreation', coordinator.create_club),   
    path('coordinator/clubcreationattempt', coordinator.club_creation_attempt)
]