from django.contrib import admin
from .models import ServiceRequestModel, ServiceReportModel, ReportPunchesModel

# Register your models here.
admin.site.register(ServiceReportModel)
admin.site.register(ServiceRequestModel)
admin.site.register(ReportPunchesModel)
