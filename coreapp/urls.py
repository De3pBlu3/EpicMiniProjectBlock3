from django.urls import path

from .views import index, auth, adminpanel, user, coordinator

urlpatterns = [
    path('', index.index),

    path('login', auth.login),
    path('loginattempt', auth.loginattempt),
    path('signupattempt', auth.signupattempt),
    
    path('admin', adminpanel.all_user_admin),
    path('admin/changeapproval', adminpanel.change_approval),
    path('admin/deregister', adminpanel.deregister),
    
    path('home', user.home),
    
 
    path('coordinator/home', coordinator.home),
    path('coordinator/clubcreation', coordinator.create_club),   
    path('coordinator/clubcreationattempt', coordinator.club_creation_attempt),
    path('coordinator/eventcreation', coordinator.create_event),
    path('coordinator/eventcreationattempt', coordinator.event_creation_attempt),

    path('user/updatedetails', user.update_user),
    path('user/updatedetailsattempt', user.update_attempt),
    path('home/clubview', user.display_clubs),
    path('home/joinclub', user.add_membership),
    path('coordinator/home', coordinator.home)
]