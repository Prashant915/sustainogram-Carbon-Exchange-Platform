from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.forms import UserChangeForm

#useradmin registration form
class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'input'}))
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'input'}))
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']
        widgets ={
            'username':forms.TextInput(attrs ={'class':'input'}),
            'first_name':forms.TextInput(attrs ={'class':'input'}),
            'last_name':forms.TextInput(attrs ={'class':'input'}),
            'email':forms.TextInput(attrs ={'class':'input'}),
        }

#useradmin profile update
class EditUserProfile(UserChangeForm):
    password=None
    class Meta:
        model= User
        fields = ['username','first_name','last_name','email','is_superuser','is_staff','is_active']#'__all__'
        widgets ={
            'username':forms.TextInput(attrs ={'class':'input','readonly': 'readonly'}),
            'first_name':forms.TextInput(attrs ={'class':'input'}),
            'last_name':forms.TextInput(attrs ={'class':'input'}),
            'email':forms.TextInput(attrs ={'class':'input'}),
            'date_joined':forms.TextInput(attrs ={'class':'input'}),
        }

