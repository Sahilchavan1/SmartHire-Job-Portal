from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, JobSeekerProfile


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'role', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control w-100'
            })


class CustomLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter email'
        })

        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter password'
        })


class JobSeekerProfileForm(forms.ModelForm):

    class Meta:
        model = JobSeekerProfile
        fields = ['full_name', 'skills', 'experience', 'bio', 'resume']

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),

            'skills': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Python, Django, MySQL'
            }),

            'experience': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '2 Years Backend Development'
            }),

            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4
            }),

            'resume': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }