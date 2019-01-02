from django import forms
from django.contrib.auth.models import User
from profile_app.models import Profile


class SignupForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['username', 'first_name', 'last_name', 'password']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'signup-username',
        'placeholder': 'username',
        'required': True
      }),
      'password': forms.PasswordInput(attrs={
        'id': 'signup-password',
        'placeholder': 'password',
        'required': True
      }),
      'first_name': forms.TextInput(attrs={
        'id': 'signup-first_name',
        'placeholder': 'first name',
        'required': True
      }),
      'last_name': forms.TextInput(attrs={
        'id': 'signup-last_name',
        'placeholder': 'last name',
        'required': True
      })
    }

class LoginForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['username', 'password']
    widgets = {
      'username': forms.TextInput(attrs={
        'id': 'login-username',
        'placeholder': 'username',
        'required': True
      }),
      'password': forms.PasswordInput(attrs={
        'id': 'login-password',
        'placeholder': 'password',
        'required': True
      })
    }

class UserForm(forms.ModelForm):
  class Meta:
    model   = User
    fields  = ['first_name', 'last_name', 'email']
    widgets = {
      'first_name': forms.TextInput(attrs={
        'id': 'user-first_name',
        'placeholder': 'first_name',
        'required': True
      }),
      'last_name': forms.TextInput(attrs={
        'id': 'user-last_name',
        'placeholder': 'last_name',
        'required': True
      }),
      'email': forms.EmailInput(attrs={
        'id': 'user-email',
        'placeholder': 'email',
        'required': True
      })
    }

class ProfileForm(forms.ModelForm):
 class Meta:
   model   = Profile
   fields  = ['bio']
   widgets = {
       'bio': forms.Textarea(attrs={
       'id': 'profile-bio',
       'placeholder': 'bio',
       'required': False
     })
   }