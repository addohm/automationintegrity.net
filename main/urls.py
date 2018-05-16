# https://docs.djangoproject.com/en/1.11/topics/http/urls/

from django.conf.urls import url, include
from django.urls import reverse_lazy
from .views import IndexView, RegisterView, ContactView, PasswordChangeView, HomeView
from .forms import LoginForm
from django.contrib.auth.views import (
    LogoutView,
    login,
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

# main app URLS extend from the base url i.e. www.website.com/*

urlpatterns = [
    url(r'^$', IndexView, name='main'),
    url(r'^home/$', HomeView, name='home'),
    url(r'^register/$', RegisterView, name='register'),
    url(r'^contact/$', ContactView, name='contact'),
    url(r'^logout/$', LogoutView.as_view(next_page=reverse_lazy('main')),
        name='logout'),
    url(r'^consultation/', include('consultation.urls')),
    # successful logins are redirected to the settings.LOGIN_REDIRECT_URL
    url(r'^login/$', login, name='login',
        kwargs={'template_name': 'main/login.html',
                'authentication_form': LoginForm}, ),
    url(r'^change_password/$',
        PasswordChangeView.as_view(
            template_name='main/change_password_form.html'),
        name='password_change'),
    url(r'^change_password/done/$',
        PasswordChangeDoneView.as_view(
            template_name='main/change_password_done.html'),
        name='password_change_done'),
    url(r'^password_reset/$', PasswordResetView.as_view(
        template_name='main/reset_password_form.html'),
        name='password_reset'),
    url(r'^password_reset/done/$', PasswordResetDoneView.as_view(
        template_name='main/reset_password_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirmView.as_view(
            template_name='main/reset_password_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done/$', PasswordResetCompleteView.as_view(
        template_name='main/reset_password_complete.html'),
        name='password_reset_complete'),
]
