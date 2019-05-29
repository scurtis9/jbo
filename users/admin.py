from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import JboUserCreationForm, JboUserChangeForm
from .models import JboUser


class JboUserAdmin(UserAdmin):
    add_form = JboUserCreationForm
    form = JboUserChangeForm
    model = JboUser
    list_display = ['email', 'username',]


admin.site.register(JboUser, JboUserAdmin)