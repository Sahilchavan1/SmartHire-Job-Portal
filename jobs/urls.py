from django.urls import path
from .views import (
    post_job,
    job_list,
    job_detail,
    apply_job,
    recruiter_jobs,
)

urlpatterns = [
    path("post-job/", post_job, name="post-job"),
    path("", job_list, name="job-list"),
    path("<int:pk>/", job_detail, name="job-detail"),
    path("<int:pk>/apply/", apply_job, name="apply-job"),
    path("my-jobs/", recruiter_jobs, name="recruiter-jobs"),
]