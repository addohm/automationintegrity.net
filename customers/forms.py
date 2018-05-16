# https://docs.djangoproject.com/en/1.11/topics/forms/

from django import forms
from django.contrib.auth.forms import (
    PasswordResetForm,
)

class ResetPasswordForm(PasswordResetForm):
    pass