from django.contrib import admin
from .models import *
# Register your models here.
class Api_Data(admin.ModelAdmin):
      list_display=('user','Vehicle_Model_No')

class EV_Usage(admin.ModelAdmin):
      list_display=('user','Vehicle_Model_No')

admin.site.register(ApiData,Api_Data)
admin.site.register(evusage,EV_Usage)