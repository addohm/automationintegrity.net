from django.shortcuts import render
from .models import ConsultationReportForm, ConsultationRequestForm


def consultation_request(request):
    form = ConsultationRequestForm(request.POST or None)
    context = {
        "form": form,
    }

    return render(request, "consultation/request.html", context)


def consultation_report(request):
    form = ConsultationReportForm(request.POST or None)
    context = {
        "form": form,
    }

    return render(request, "consultation/report.html", context)
