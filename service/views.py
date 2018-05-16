from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.shortcuts import render, redirect
from .forms import (
    ServiceReportCreateForm,
    ServiceReportUpdateForm,
    # ServiceRequestCreateForm,
    # ServiceRequestUpdateForm
)
from .models import ServiceReportModel, ServiceRequestModel


'''
Service request forms for customers to
request service
'''


class RequestListView(ListView):
    model = ServiceRequestModel
    template_name = 'service/request-list.html'


class RequestDetailView(DetailView):
    model = ServiceRequestModel
    template_name = 'service/request-detail.html'


# class RequestUpdateView(UpdateView):
#     form_class = ServiceRequestUpdateForm
#     model = ServiceRequestModel


class RequestDeleteView(DeleteView):
    model = ServiceRequestModel
    template_name = 'service/delete-confirm.html'
    success_url = reverse_lazy('service:request-list')
    success_message = 'The request has successfully been deleted.'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(RequestDeleteView, self).delete(request, *args, **kwargs)


'''
Service report forms for employees to
report service
'''


class ReportListView(ListView):
    model = ServiceReportModel
    template_name = 'service/report-list.html'


class ReportDetailView(DetailView):
    model = ServiceReportModel
    template_name = 'service/report-detail.html'


class ReportUpdateView(UpdateView):
    template_name = 'service/report-update.html'
    form_class = ServiceReportUpdateForm 
    model = ServiceReportModel


class ReportCreateView(View):
    model = ServiceReportModel
    form_class = ServiceReportCreateForm
    template_name = 'service/report-create.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service:report-list')

        return render(request, self.template_name, {'form': form})




#class ReportUpdateView(View):
#    template_name = 'service/report-update.html'
#    form_class = ServiceReportCreateForm  # (initial={'request_number': '---------------'})
#    model = ServiceReportModel

#    def get(self, request, *args, **kwargs):
#        form = self.form_class
#         return render(request, self.template_name, {'form': form})

#    def post(self, request, *args, **kwards):
#        form = self.form_class(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('service:report-list')

#        return render(request, self.template_name, {'form', form})


class ReportDeleteView(DeleteView):
    model = ServiceReportModel
    template_name = 'service/delete-confirm.html'
    success_url = reverse_lazy('service:report-list')
    success_message = 'The report has successfully been deleted.'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ReportDeleteView, self).delete(request, *args, **kwargs)
