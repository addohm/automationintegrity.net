# https://docs.djangoproject.com/en/1.11/topics/http/views/
# https://docs.djangoproject.com/en/1.11/topics/class-based-views/

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import (
    logout,
    login,
    authenticate,
    update_session_auth_hash
)
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import PasswordChangeForm
from django.core.mail import send_mail

from .models import MyUser
from .forms import RegistrationForm, LoginForm, ResetPasswordForm, ContactForm


def HomeView(request):
    return render(request, 'main/userhome.html')


def IndexView(request):
    return render(request, 'main/index.html')


def ContactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            cc_myself = form.cleaned_data['cc_myself']
            message = form.cleaned_data['message']
            pass # do something with data
        pass
    else:
        form = ContactForm()
        return render(request, 'main/contact.html')


def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = LoginForm()
        args={ 'form': form }
    return render(request, 'main/login.html', args)


def LogoutView(request):
    logout(request)

@login_required
def PasswordChangeView(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, form.user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_password_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'main/change_password_form.html', {
        'form': form
    })
    #return render(request, 'main/password_change_form.html')


# @permission_required(['auth.add_customuser', 'auth.change_customuser'], raise_exception=True)
def RegisterView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('main')
    else:
        form = RegistrationForm()

    args = {'form': form}
    return render(request, 'main/register.html', args)
