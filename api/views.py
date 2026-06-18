from rest_framework import viewsets, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from jobs.models import Job
from applications.models import Application

from .serializers import JobSerializer
from .permissions import IsRecruiterOrReadOnly


class JobViewSet(viewsets.ModelViewSet):

    serializer_class = JobSerializer
    permission_classes = [IsRecruiterOrReadOnly]

    def get_queryset(self):
        return Job.objects.filter(is_approved=True)

    def perform_create(self, serializer):
        serializer.save(recruiter=self.request.user)


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def apply_job_api(request, pk):

    if request.user.role != 'job_seeker':
        return Response(
            {"error": "Only job seekers can apply."},
            status=status.HTTP_403_FORBIDDEN
        )

    job = get_object_or_404(Job, pk=pk, is_approved=True)

    if Application.objects.filter(job=job, job_seeker=request.user).exists():
        return Response(
            {"message": "You already applied."},
            status=status.HTTP_400_BAD_REQUEST
        )

    Application.objects.create(job=job, job_seeker=request.user)

    return Response(
        {"message": "Application submitted successfully!"},
        status=status.HTTP_201_CREATED
    )