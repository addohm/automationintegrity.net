from django.conf.urls import url
from .views import consultation_request, consultation_report

app_name = 'consultation'

urlpatterns = [
   url(r'^request/$', consultation_request, name='request'),
   url(r'^report/$', consultation_report, name='report'),
]