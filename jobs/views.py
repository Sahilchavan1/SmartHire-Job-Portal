from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q

from .forms import JobForm
from .models import Job
from applications.models import Application


@login_required
def post_job(request):

    if request.user.role != "recruiter":
        messages.error(request, "Only recruiters can post jobs.")
        return redirect("redirect-dashboard")

    if request.method == "POST":
        form = JobForm(request.POST)

        if form.is_valid():
            job = form.save(commit=False)
            job.recruiter = request.user
            job.save()

            messages.success(
                request,
                "Job posted successfully! Waiting for admin approval."
            )

            return redirect("recruiter-dashboard")

    else:
        form = JobForm()

    return render(request, "jobs/post_job.html", {"form": form})


def job_list(request):

    jobs = Job.objects.filter(is_approved=True)

    search = request.GET.get("search")
    location = request.GET.get("location")
    job_type = request.GET.get("job_type")

    if search:
        jobs = jobs.filter(title__icontains=search)

    if location:
        jobs = jobs.filter(location__icontains=location)

    if job_type:
        jobs = jobs.filter(job_type=job_type)

    paginator = Paginator(jobs, 5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        "jobs/job_list.html",
        {"page_obj": page_obj}
    )


def job_detail(request, pk):

    job = get_object_or_404(Job, id=pk)

    has_applied = False

    if request.user.is_authenticated and request.user.role == "job_seeker":
        has_applied = Application.objects.filter(
            job=job,
            job_seeker=request.user
        ).exists()

    return render(
        request,
        "jobs/job_detail.html",
        {
            "job": job,
            "has_applied": has_applied
        }
    )


@login_required
def apply_job(request, pk):

    if request.user.role != "job_seeker":
        messages.error(request, "Only job seekers can apply.")
        return redirect("redirect-dashboard")

    job = get_object_or_404(Job, pk=pk)

    if Application.objects.filter(job=job, job_seeker=request.user).exists():
        messages.warning(request, "You already applied for this job.")
        return redirect("job-list")

    Application.objects.create(job=job, job_seeker=request.user)

    messages.success(request, "Applied successfully!")

    return redirect("job-list")


@login_required
def recruiter_jobs(request):

    if request.user.role != "recruiter":
        return redirect("redirect-dashboard")

    jobs = Job.objects.filter(recruiter=request.user)

    return render(
        request,
        "jobs/recruiter_jobs.html",
        {"jobs": jobs}
    )