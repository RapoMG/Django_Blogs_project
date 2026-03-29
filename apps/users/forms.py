from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

from users.models import Profile

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    # password fields are at this level within parent class
    class Meta(UserCreationForm.Meta):  # Inherits from UserCreationForm.Meta not replaces as Meta(), so it keeps other properties like help_texts.
        model = User
        fields = ("username", "email")


class CustomAuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile  # Access the related Profile model through the User model
        fields = ['avatar', 'description', 'is_email_visible']

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']
