from django.urls import path

from .views import index, auth, adminpanel, user, coordinator

urlpatterns = [
    path('', index.index),

    path('dummy_login', auth.dummy_login),
    path('login', auth.login),
    path('loginattempt', auth.loginattempt),
    path('admin', adminpanel.all_user_admin),
    
    
    path('home', user.home),
    
    path('coordinator/home', coordinator.home)
]