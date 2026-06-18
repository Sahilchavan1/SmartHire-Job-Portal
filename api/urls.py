from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import JobViewSet, apply_job_api


router = DefaultRouter()
router.register(r'jobs', JobViewSet, basename='jobs')


urlpatterns = [
    path('', include(router.urls)),
    path('jobs/<int:pk>/apply/', apply_job_api, name='api-apply-job'),
    path('login/', obtain_auth_token, name='api-login'),
]