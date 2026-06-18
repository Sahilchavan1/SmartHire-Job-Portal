from rest_framework import serializers
from jobs.models import Job


class JobSerializer(serializers.ModelSerializer):

    recruiter_email = serializers.ReadOnlyField(source="recruiter.email")

    class Meta:
        model = Job

        fields = [
            "id",
            "title",
            "description",
            "salary",
            "location",
            "job_type",
            "is_approved",
            "created_at",
            "recruiter_email",
        ]

        read_only_fields = ["is_approved", "created_at"]