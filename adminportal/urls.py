from django.urls import path
from . import views 

urlpatterns = [
    path('',views.sign_in.as_view(),name='userlogin'),
    path('user-signup/',views.sign_up,name='usersignup'),
    path('userprofile/',views.userprofile,name='userprofile'),
    path('userdashboard/',views.userdashboard,name='userdashboard'),

    path('userauth/<int:id>/',views.allprofile,name='userauth'),
    path('delprofile/<int:id>/',views.delprofile,name='delprofile'),
    path('allusers/',views.user_data,name='allusers'),
    path('userissuence/',views.proissuence,name='userissuence'),
    
    path('issuence-detail/<int:id>',views.issuencedetails,name='issuence-detail'),
    path('delissuence/<int:id>',views.delissuence,name='delissuence'),
    # path('logout/',views.attempt_logout,name='logout'),
]