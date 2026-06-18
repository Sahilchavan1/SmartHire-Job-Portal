from django import forms
from .models import Job


class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = [
            "title",
            "company_name",
            "description",
            "location",
            "salary",
            "experience_required",
            "skills_required",
            "qualification",
            "vacancy",
            "job_type",
            "application_deadline",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

        self.fields["description"].widget.attrs.update({"rows": 4})
        self.fields["skills_required"].widget.attrs.update({"rows": 3})