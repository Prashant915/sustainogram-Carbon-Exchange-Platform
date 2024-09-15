from django.urls import path
from . import views 

urlpatterns = [
    path('',views.Afforestation,name="afforestation"),
    path('projectestablishment/',views.project_establish,name="projectestablish"),
    path('datadelete/<int:pk>',views.deldata,name='datadelete'),
    path('monitorsurvival/',views.monitor_survival,name='monitorsurvival'),
]