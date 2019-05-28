from django import forms
from django.forms.models import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment

        fields = ['author', 'body', 'post']

        widgets = {'post': forms.HiddenInput()}