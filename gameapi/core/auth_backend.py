from django.contrib.auth.backends import BaseBackend

from .models import MyUser

class AuthenticationWithoutPassword(BaseBackend):

    def authenticate(self, request, username=None, email=None):
        if username is None:
            username = request.data.get('username', '')
            email = request.data.get('email', '')
        try:
            return MyUser.objects.get(username=username, email=email)
        except MyUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return MyUser.objects.get(pk=user_id)
        except MyUser.DoesNotExist:
            return None