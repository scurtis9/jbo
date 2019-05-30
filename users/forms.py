from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import JboUser, Profile


class JboUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = JboUser
        fields = ('username', 'email', 'first_name', 'last_name')


class JboUserChangeForm(UserChangeForm):

    class Meta:
        model = JboUser
        fields = ('username', 'email')


class ProfileChangeForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image']