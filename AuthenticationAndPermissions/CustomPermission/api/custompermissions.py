from rest_framework.permissions import BasePermission


# this is custom permission class where we can tell at which request give permission also to which user (User should be authenticated for post ,put etc request)
class MyPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.method=="GET":
            return True
        return False
    