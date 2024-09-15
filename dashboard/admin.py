from django.contrib import admin
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from .forms import *
# Register your models here.
class Profiles(admin.ModelAdmin):
      list_display=('user','email','country','mobile','company')

admin.site.register(User_Profile,Profiles)

class issuence_Display(admin.ModelAdmin):
      list_display=("S_ID","Project_Name","POA_S_ID","Issuence_Date")

admin.site.register(Issuence,issuence_Display)

# class CustomUserAdmin(UserAdmin):
#     form = CustomUserChangeForm  # Use the custom form

#     fieldsets = (
#         (None, {'fields': ('username', 'password')}),
#         ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#     )

# Unregister the existing User model
# admin.site.unregister(User)

# Register the User model with the CustomUserAdmin
# admin.site.register(User, CustomUserAdmin)



