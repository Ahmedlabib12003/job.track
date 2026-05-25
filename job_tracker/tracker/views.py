from django.shortcuts import render
from .models import JobApplication
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


# Create your views here.
class dashboard(ListView):
    template_name = "tracker/dashboard.html"
    model = JobApplication
    context_object_name = "applications"


class create(CreateView):
    template_name = "tracker/form.html"
    model = JobApplication
    fields = ["company_name", "job_title", "status", "job_url", "notes"]
    success_url = reverse_lazy('tracker:dashboard')


class update(UpdateView):
    template_name = "tracker/form.html"
    model = JobApplication
    fields = ["company_name", "job_title", "status", "job_url", "notes"]
    success_url = reverse_lazy('tracker:dashboard')