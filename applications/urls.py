from django.urls import path

from .views import (
    my_applications,
    view_applicants,
    update_status
)

urlpatterns = [
    path("my-applications/", my_applications, name="my-applications"),
    path("job/<int:pk>/applicants/", view_applicants, name="view-applicants"),
    path("update-status/<int:app_id>/<str:status>/", update_status, name="update-status"),
]