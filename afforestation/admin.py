from django.contrib import admin
from .models import *

class Trees_Planted(admin.ModelAdmin):
      list_display=('user','Project_Name')

class Species(admin.ModelAdmin):
      list_display=('user','Species_Planted')

admin.site.register(Planted_trees,Trees_Planted)
admin.site.register(Trees_Species,Species)
