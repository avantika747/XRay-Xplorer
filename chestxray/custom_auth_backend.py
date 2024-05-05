from django.contrib.auth.backends import BaseBackend
from .models import Doctor

''' This code is to override the custom Backend Authentication that Django offers. This code was modified to 
allow access only to the doctors whose profiles were created by the superuser option of Django. Upon login, if
the credentials match those of the superusers, the user is allowed access to the dashboard. If not, they get 
redirected to the login page. '''

class CustomAuthBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Doctor.objects.get(username=username)
            if user.is_superuser and user.username in ['superuser1', 'superuser2', 'superuser3', 'superuser4']:
                if user.check_password(password):
                    return user
        
        except Doctor.DoesNotExist:
            return None
