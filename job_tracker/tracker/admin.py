from django.contrib import admin
from .models import JobApplication
admin.site.site_header = "Job Applications Administrator Page"
admin.site.site_title = "Job Applications Admin"

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ["company_name", "job_title", "status", "date_applied"]
    list_filter = ["status"]
    search_fields = ["company_name"]
