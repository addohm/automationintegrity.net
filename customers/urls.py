# https://docs.djangoproject.com/en/1.11/topics/http/urls/

from django.conf.urls import url

from .views import CompanyDetailView, SiteDetailView, CompanyListView

app_name = 'customers'

urlpatterns = [
   url(r'^$', CompanyListView.as_view(),
       name='company-list'),
   url(r'^(?P<pk>[0-9a-z-]+)/detail/$', CompanyDetailView.as_view(),
       name='company-detail'),
   url(r'^(?P<pk>[0-9a-z-]+)/detail/site/$', SiteDetailView.as_view(),
       name='site-detail'),
   # url(r'^maps/$', relative_distance, name='maps'),
]
