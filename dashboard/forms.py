from django import forms
from django.contrib.auth.models import User

# class CustomUserChangeForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = '__all__'

#     # Override the is_staff field
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['is_staff'].label = "Consultant"
#         self.fields['is_staff'].help_text = "Designates whether the user is a consultant and can register projects."
