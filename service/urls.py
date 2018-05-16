from django.conf.urls import url
from .views import (
    RequestListView,
    RequestDetailView,
    # RequestCreateView,
    # RequestUpdateView,
    RequestDeleteView,
    ReportListView,
    ReportDetailView,
    ReportCreateView,
    ReportUpdateView,
    ReportDeleteView,
)

app_name = 'service'

urlpatterns = [
    url(r'^requests/$', RequestListView.as_view(), name='request-list'),
    # url(r'^request/new/$', RequestCreateView.as_view(), name='new-request'),
    url(r'^request/(?P<pk>[0-9a-z-]+)/detail/$',
        RequestDetailView.as_view(), name='request-detail'),
    # url(r'^request/(?P<pk>[0-9a-z-]+)/update/$', RequestUpdateView.as_view(), name='update-request'),
    url(r'^request/(?P<pk>[0-9a-z-]+)/delete/$',
        RequestDeleteView.as_view(), name='delete-request'),
    url(r'^reports/$', ReportListView.as_view(), name='report-list'),
    url(r'^report/new/$', ReportCreateView.as_view(), name='new-report'),
    url(r'^report/(?P<pk>[0-9a-z-]+)/detail/$',
        ReportDetailView.as_view(), name='report-detail'),
    url(r'^report/(?P<pk>[0-9a-z-]+)/update/$',
        ReportUpdateView.as_view(), name='update-report'),
    url(r'^report/(?P<pk>[0-9a-z-]+)/delete/$',
        ReportDeleteView.as_view(), name='delete-report'),
]
