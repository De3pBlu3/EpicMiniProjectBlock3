from django.urls import path

from .views import index, auth, adminpanel, user, coordinator, clubMgnt

urlpatterns = [
    path('', index.index),

    path('login', auth.login),
    path('loginattempt', auth.loginattempt),
    path('signupattempt', auth.signupattempt),
    
    path('admin', adminpanel.all_user_admin),
    path('admin/changeapproval', adminpanel.user_change_approval),
    path('admin/deregister', adminpanel.user_deregister),
    path('admin/changeclubapproval', adminpanel.club_change_approval),    
 
    path('coordinator/home', coordinator.home),
    path('coordinator/clubcreation', coordinator.create_club),   
    path('coordinator/clubcreationattempt', coordinator.club_creation_attempt),
  
    path('coordinator/eventcreation', coordinator.create_event),
    path('coordinator/eventcreationattempt', coordinator.event_creation_attempt),
  
    path('coordinator/venuecreation', coordinator.venue_creation),
    path('coordinator/venuecreationattempt', coordinator.venue_creation_attempt),
  
    path('coordinator/clubmanagement', clubMgnt.coordinator_club_mgnt),
    path('coordinator/clubmanagement/changeapproval', clubMgnt.user_change_approval),
    path('coordinator/clubmanagement/deregister', clubMgnt.user_deregister),
    path('coordinator/clubmanagement/eventchangeapproval', clubMgnt.event_attendance_change_approval),
  
    path('user/updatedetails', user.update_user),
    path('user/updatedetailsattempt', user.update_attempt),

    path('home', user.home),
    path('user/updatedetails', user.update_user),
    path('user/updatedetailsattempt', user.update_attempt),
    path('user/addeventapplication', user.add_event_application),
    path('home/clubview', user.display_clubs),
    path('home/joinclub', user.add_membership)
]