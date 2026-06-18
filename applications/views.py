from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from .models import Application
from jobs.models import Job


@login_required
def my_applications(request):

    if request.user.role != "job_seeker":
        return redirect("redirect-dashboard")

    applications = Application.objects.filter(
        job_seeker=request.user
    ).order_by("-applied_at")

    return render(
        request,
        "applications/my_applications.html",
        {"applications": applications},
    )


@login_required
def view_applicants(request, pk):

    job = get_object_or_404(Job, pk=pk)

    if request.user != job.recruiter:
        return redirect("redirect-dashboard")

    applications = Application.objects.filter(job=job)

    return render(
        request,
        "applications/view_applicants.html",
        {
            "job": job,
            "applications": applications,
        },
    )


@login_required
def update_status(request, app_id, status):

    application = get_object_or_404(Application, id=app_id)

    application.status = status
    application.save()

    job = application.job
    applicant = application.job_seeker

    subject = f"Application Update for {job.title}"

    if status == "shortlisted":
        message = f"""
Hello {applicant.email},

Congratulations!

Your application for the position of "{job.title}" at {job.company_name} has been shortlisted.

The recruiter may contact you soon regarding the next steps.

Job Details:
Position: {job.title}
Company: {job.company_name}
Location: {job.location}

Best regards,
SmartHire Team
"""

    elif status == "rejected":
        message = f"""
Hello {applicant.email},

Thank you for applying for "{job.title}" at {job.company_name}.

After review, the recruiter has decided not to move forward with your application.

We encourage you to keep applying to other opportunities on SmartHire.

Best wishes,
SmartHire Team
"""

    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [applicant.email],
        fail_silently=True,
    )

    return redirect("view-applicants", pk=job.id)