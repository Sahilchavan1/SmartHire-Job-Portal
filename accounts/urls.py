from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import CustomLoginForm
from .views import redirect_dashboard, jobseeker_dashboard, recruiter_dashboard


urlpatterns = [
    path('register/', views.register, name='register'),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='accounts/login.html',
            authentication_form=CustomLoginForm
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),

    path('dashboard/', redirect_dashboard, name='redirect-dashboard'),
    path('jobseeker/', jobseeker_dashboard, name='jobseeker-dashboard'),
    path('recruiter/', recruiter_dashboard, name='recruiter-dashboard'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
]