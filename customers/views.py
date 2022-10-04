from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import SiteModel, CompanyModel, ContactModel
from service.models import ServiceReportModel
import googlemaps


class CompanyDetailView(DetailView):
    model = CompanyModel
    context_object_name = 'company'
    template_name = 'customers/company-detail.html'

    def get_context_data(self, **kwargs):
            context = super(CompanyDetailView, self).get_context_data(**kwargs)
            context['sites'] = SiteModel.objects.filter(company=self.get_object())
            context['contacts'] = ContactModel.objects.filter(site__company=self.get_object())
            context['reports'] = ServiceReportModel.objects.filter(site__company=self.get_object())
            return context


class CompanyListView(ListView):
    model = CompanyModel
    context_object_name = 'companies'
    template_name = 'customers/company-list.html'


class SiteDetailView(DetailView):
    model = SiteModel
    context_object_name = 'site'
    template_name = 'customers/site-detail.html'

    def get_context_data(self, **kwargs):
            context = super(SiteDetailView, self).get_context_data(**kwargs)
            # context['company'] = CompanyModel.objects.filter(site=self.get_object())
            context['reports'] = ServiceReportModel.objects.filter(site=self.get_object())
            context['contacts'] = ContactModel.objects.filter(site=self.get_object())
            return context


def relative_distance(request, *args, **kwargs):
        gmaps = googlemaps.Client(key='')
        origin = 'quincy, ma'
        destination = 'lowell, ma'
        template_name = 'maps.html'
        distance = gmaps.distance_matrix(origin, destination)
        return render(request, template_name, {
            'origin': origin,
            'destination': destination,
            'distance': distance,
        })
