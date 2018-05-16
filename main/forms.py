# https://docs.djangoproject.com/en/1.11/topics/forms/

from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    UserCreationForm,
    UserChangeForm,
    PasswordResetForm,
)
from .models import MyUser


class ResetPasswordForm(PasswordResetForm):
    pass


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username',
                               widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = MyUser
        fields = (
            'username',
            'firstName',
            'lastName',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['firstName']
        user.last_name = self.cleaned_data['lastName']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100, required=True, label='Subject',
                              widget=forms.TextInput(attrs={
                                  'class=': 'form-control',
                                  'placeholder': 'Enter a subject',
                                  'required': 'true'})
                              )
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(required=True, label='E-Mail')
    cc_myself = forms.BooleanField(required=False, label='CC Myself', label_suffix='?')
    message = forms.CharField(widget=forms.Textarea, required=True, label='Subject')
