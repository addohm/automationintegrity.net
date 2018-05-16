import uuid
from django.db import models
from django.forms import ModelForm
from main import models as main_models
from customers import models as customerc_models

# Create your models here.

"""
Consultation Requests
Consultation Request Form
•	Date\Time
•	Company Name
•	Contact Name 
•	Phone Number®
•	Email Address®
•	Concept\Description
"""

class ConsultationRequestModel(models.Model):
    request_number = models.UUIDField(primary_key=True,
                                      default=uuid.uuid4,
                                      editable=False
                                     )
    requester = models.ForeignKey(main_models.MyUser,
                                  on_delete=models.PROTECT,
                                  related_name='c_request_requester'
                                 )
    request_date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(customerc_models.CompanyModel,
                                on_delete=models.PROTECT,
                                related_name='c_request_company'
                               )
    site = models.ForeignKey(customerc_models.SiteModel,
                             on_delete=models.PROTECT,
                             related_name='c_request_site'
                            )
    contact = models.ForeignKey(customerc_models.ContactModel,
                                on_delete=models.PROTECT,
                                related_name='c_request_contact'
                               )
    phone_number = models.ForeignKey(customerc_models.PhoneModel,
                                     on_delete=models.PROTECT,
                                     related_name='c_request_phone'
                                    )
    request_description = models.TextField()


class ConsultationRequestForm(ModelForm):
    class Meta:
        model = ConsultationRequestModel
        fields = ['requester', 'company', 'site', 'contact',
                  'phone_number', 'request_description'
                 ]


"""
Consultation Reports
•	Notes
•	Recommendations
"""

class ConsultationReportModel(models.Model):
    report_number = models.UUIDField(primary_key=True,
                                     default=uuid.uuid4,
                                     editable=False
                                    )
    request_number = models.ForeignKey(ConsultationRequestModel,
                                       on_delete=models.PROTECT,
                                       null=True,
                                       related_name='c_report_number'
                                      )
    notes = models.TextField()
    recommendations = models.TextField()


class ConsultationReportForm(ModelForm):
    class Meta:
        model = ConsultationReportModel
        fields = ['request_number', 'notes', 'recommendations']
