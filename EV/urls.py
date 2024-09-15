from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Electricvehicle,name="electricvehicle"),
    path('datatable/',views.datapoints,name="datatable"),
    path('datadelete/<int:pk>',views.deldata,name='datadelete'),
    path('evusage/',views.evusages,name='evusage'),
]