from django.db import models


class JobApplication(models.Model):
    STATUS_CHOICES = [
        ("APPLIED", "Applied"),
        ("INTERVIEW", "Interviewing"),
        ("OFFER", "Offer"),
        ("REJECTED", "Rejected"),
    ]

    company_name = models.CharField(max_length=30)
    job_title = models.CharField(max_length=30)
    status = models.CharField(choices=STATUS_CHOICES)
    date_applied = models.DateField(auto_now_add=True)
    job_url = models.URLField()
    notes = models.TextField(blank=True)
