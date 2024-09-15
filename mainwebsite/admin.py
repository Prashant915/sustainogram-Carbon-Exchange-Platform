from django.contrib import admin
from .models import *
from django.utils.html import mark_safe


class Resources(admin.ModelAdmin):
    list_display=('Resource_image','Title')
    def Resource_image(self,obj):
            return mark_safe(f'<img src="/media/{obj.Image}" width="150" height="120"/>')
    
admin.site.register(resource,Resources)