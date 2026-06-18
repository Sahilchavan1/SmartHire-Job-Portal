from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegisterForm, JobSeekerProfileForm
from .models import JobSeekerProfile
from applications.models import Application


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


@login_required
def redirect_dashboard(request):
    if request.user.role == 'job_seeker':
        return redirect('jobseeker-dashboard')

    elif request.user.role == 'recruiter':
        return redirect('recruiter-dashboard')

    else:
        return redirect('admin:index')


@login_required
def jobseeker_dashboard(request):
    applications = Application.objects.filter(
        job_seeker=request.user
    ).order_by('-applied_at')[:5]

    context = {
        'applications': applications
    }

    return render(request, 'accounts/jobseeker_dashboard.html', context)


@login_required
def recruiter_dashboard(request):
    return render(request, 'accounts/recruiter_dashboard.html')


@login_required
def edit_profile(request):
    profile, created = JobSeekerProfile.objects.get_or_create(
        user=request.user
    )

    if request.method == 'POST':
        form = JobSeekerProfileForm(
            request.POST,
            request.FILES,
            instance=profile
        )

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('jobseeker-dashboard')
    else:
        form = JobSeekerProfileForm(instance=profile)

    context = {
        'form': form
    }

    return render(request, 'accounts/edit_profile.html', context)