from django.urls import path
from . import views 

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('service/',views.contentview.as_view(template_name='website/service.html'),name='service'),
    path('about/',views.contentview.as_view(template_name='website/about.html'),name='about'),
    path('resource/',views.resources,name='resource'),

    path('calculator/',views.contentview.as_view(template_name='website/calculator.html'),name='calculator'),
    path('contact/',views.contentview.as_view(template_name='website/contact.html'),name='contact'),
    path('carbon-policy/',views.contentview.as_view(template_name='website/privacy-policy.html'),name='policy'),
    path('achivements/',views.contentview.as_view(template_name='website/achievements.html'),name="achivements"),
    path('whitepaper/',views.contentview.as_view(template_name='website/white-paper.html'),name="whitepaper"),
    path('carbonexchange/',views.contentview.as_view(template_name='website/carbonexchange.html'),name='carbonexchange'),
    path('summery/<int:resourceid>',views.summery,name='summery')
]
