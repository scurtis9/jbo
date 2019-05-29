from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import JboUser


class JboUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = JboUser
        fields = ('username', 'email')


class JboUserChangeForm(UserChangeForm):

    class Meta:
        model = JboUser
        fields = ('username', 'email')