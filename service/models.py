import uuid
from django.urls import reverse
from django.db import models
from main import models as main_models
from customers import models as customers_models


"""
Service Requests
Service Request Form CUSTOMER
•	Date/Time
•	Company Name
•	Contact Name
•	Phone Number®
•	Email Address®
•	Equipment
•	Description
"""


class ServiceRequestModel(models.Model):
    request_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    requested_by = models.ForeignKey(main_models.MyUser,
                                     on_delete=models.PROTECT,
                                     related_name='s_request_requester'
                                     )
    requested_date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(customers_models.CompanyModel,
                                on_delete=models.PROTECT,
                                related_name='s_request_company'
                                )
    site = models.ForeignKey(customers_models.SiteModel,
                             on_delete=models.PROTECT,
                             related_name='s_request_site'
                             )
    contact = models.ForeignKey(customers_models.ContactModel,
                                on_delete=models.PROTECT,
                                related_name='s_request_contact',
                                null='True',
                                blank='True'
                                )
    phone_number = models.ForeignKey(customers_models.PhoneModel,
                                     on_delete=models.PROTECT,
                                     related_name='s_request_phone'
                                     )
    equipment = models.ForeignKey(customers_models.EquipmentModel,
                                  on_delete=models.PROTECT,
                                  related_name='s_equipment')
    severity = models.SmallIntegerField(null=False, blank=False)
    request_description = models.TextField()
    completed = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('service-request', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s %s, %s - %s' % ('Complete' if self.completed else 'Incomplete',
                                   self.company,
                                   self.equipment.name,
                                   self.requested_date.strftime('%d %B %Y'))

    class Meta:
        ordering = ['requested_date', 'completed']
        verbose_name = 'Service Request'
        verbose_name_plural = 'Service Requests'


"""
Service Reports
Service Report Form ADMIN
•	Reason for Report
•	Actions Taken
"""


class ServiceReportModel(models.Model):
    report_number = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    site = models.ForeignKey(customers_models.SiteModel,
                             on_delete=models.PROTECT, related_name='reports')
    request_number = models.ForeignKey(ServiceRequestModel,
                                       on_delete=models.PROTECT,
                                       null=True,
                                       blank=True,
                                       related_name='s_report_number'
                                       )
    reported_by = models.ForeignKey(
        main_models.MyUser, related_name='reporter',
        on_delete=models.PROTECT)
    reported_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(
        main_models.MyUser,
        blank=True,
        null=True,
        related_name='updater',
        on_delete=models.PROTECT)
    updated_date = models.DateTimeField(auto_now=True)
    equipment = models.ForeignKey(
        customers_models.EquipmentModel, on_delete=models.PROTECT)
    report_reason = models.CharField(max_length=255, null=True)
    actions_taken = models.TextField(null=False, blank=False)
    recommendations = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return reverse('service-report', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s - %s, %s' % (self.site.company,
                                self.reported_date.strftime('%d %B %Y'),
                                self.equipment.name
                                )

    class Meta:
        ordering = ['reported_date']
        verbose_name = 'Service Report'
        verbose_name_plural = 'Service Reports'


class ReportPunchesModel(models.Model):
    report = models.ForeignKey(ServiceReportModel, on_delete=models.PROTECT)
    time_in = models.DateTimeField(blank=True, null=True)
    time_out = models.DateTimeField(blank=True, null=True)
