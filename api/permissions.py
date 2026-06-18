from rest_framework import permissions


class IsRecruiterOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):

        # Allow read requests for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only recruiters can create jobs
        return request.user.is_authenticated and request.user.role == "recruiter"

    def has_object_permission(self, request, view, obj):

        # Allow read requests
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only the recruiter who created the job can modify it
        return obj.recruiter == request.user