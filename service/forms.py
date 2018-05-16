from django import forms
from functools import partial
# from bootstrap3_datetime.widgets import DateTimePicker
# from django.forms.widgets import SplitDateTimeWidget
from .models import ServiceReportModel, ServiceRequestModel, ReportPunchesModel


DateInput = partial(forms.DateInput, {'class': 'datepicker'})


class ServiceReportCreateForm(forms.ModelForm):

    class Meta:
        model = ServiceReportModel
        fields = [
            'site',
            'request_number',
            'reported_by',
            # Instead I think I would like to show existing
            # punches and add links to a popup
            # that allows you to add punches
            #
            # 'time_in',
            # 'time_out',
            'equipment',
            'report_reason',
            'actions_taken',
            'recommendations',
        ]
        widgets = {
            'site': forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputSite',
            }),
            'request_number': forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputRequest',
            }),
            'reported_by': forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputReporter',
            }),
            # 'time_in': forms.DateTimeInput(attrs={
            #     'class': 'form-control',
            # }),
            # 'time_out': forms.DateTimeInput(attrs={
            #     'class': 'form-control',
            # }),
            'equipment': forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputEquipment',
            }),
            'report_reason': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Reason for Service Report'}),
            'actions_taken': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'To the best of your abilities, list all actions taken during service.  Please include' +
                'dates, times, and equipment names'}),
            'recommendations': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'If any recommendations were made to the customer that'
                               'require follow-up itemize them here...'}),
        }

        def __init__(self, *args, **kwargs):
            super(ServiceReportCreateForm, self).__init__(*args, **kwargs)
            self.fields['request_number'].required = False


class ServiceReportUpdateForm(forms.ModelForm):

    class Meta:
        model = ServiceReportModel
        fields = [
            'site',
            'request_number',
            'updated_by',
#            'time_in',
#            'time_out',
            'equipment',
            'report_reason',
            'actions_taken',
            'recommendations',
        ]
        widgets = {
            'site': forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputSite',
            }),
            'request_number': forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputRequest',
            }),
            'updated_by': forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputReporter',
            }),
#            'time_in': forms.DateTimeInput(attrs={
#                'class': 'form-control',
#            }),
#            'time_out': forms.DateTimeInput(attrs={
#                'class': 'form-control',
#            }),
            'equipment': forms.Select(attrs={
                'class': 'form-control',
                'id': 'inputEquipment',
            }),
            'report_reason': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Reason for Service Report'}),
            'actions_taken': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'To the best of your abilities, list all actions taken during service.  Please include' +
                'dates, times, and equipment names'}),
            'recommendations': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'If any recommendations were made to the customer that'
                               'require follow-up itemize them here...'}),
        }

        def __init__(self, *args, **kwargs):
            super(ServiceReportUpdateForm, self).__init__(*args, **kwargs)
            self.fields['request_number'].required = False
