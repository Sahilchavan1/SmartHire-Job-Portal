from django.contrib import admin
from .models import Job


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'recruiter', 'job_type', 'is_approved', 'created_at')
    list_filter = ('job_type', 'is_approved')
    search_fields = ('title', 'location')