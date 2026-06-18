from django.db import models
from django.conf import settings


class Job(models.Model):

    JOB_TYPE_CHOICES = [
        ("full_time", "Full Time"),
        ("part_time", "Part Time"),
        ("internship", "Internship"),
        ("contract", "Contract"),
        ("remote", "Remote"),
    ]

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)

    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=100)

    experience_required = models.CharField(max_length=100)
    skills_required = models.TextField()
    qualification = models.CharField(max_length=255)

    vacancy = models.PositiveIntegerField(default=1)
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)

    application_deadline = models.DateField(null=True, blank=True)

    is_approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    recruiter = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.title} - {self.company_name}"