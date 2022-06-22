from rest_framework.permissions import SAFE_METHODS, BasePermission
from .models import Profile

class IsUpdateProfile(BasePermission):

      def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # obj here is a UserProfile instance
        return request.user == Profile.objects.get(pk=view.kwargs['pk'])
