from django.urls import path
from . import views 

urlpatterns = [
    path('',views.dashboard,name='homedashboard'),
    path('registry/',views.dashboard2,name='dashboard2'),
    path('retirement/',views.retirement,name='retirement'),
    path('issuence/',views.issuence,name='issuence'),
    path('allprojects/',views.projects,name='allprojects'),
    path('clientregister/',views.client_register.as_view(),name='clientregister'),
    path('creditblock/',views.detailing,name='creditblock'),
    path('userlogin/',views.log_in.as_view(),name='login'),
    path('user-register/',views.register.as_view(),name='register'),

    path('project-type/<str:project>/', views.projectsfilter, name='projects'),
    
    path('user-profile/',views.profile,name='profile'),
    path('logout/',views.attempt_logout,name='logout'),
]