from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from chestxray.models import Doctor

''' This code allows one to create superusers for permitting access to the login'''

class Command(BaseCommand):
    help = 'Creates users'

    def handle(self, *args, **kwargs):
        Doctor.objects.create_user(username='Meredith_Grey', email='mgrey@seattlegrace.com', password='epompeo')
        Doctor.objects.create_user(username='Christina_Yang', email='cyang@seattlegrace.com', password='soh')
        Doctor.objects.create_user(username='Derek_Shepherd', email='dshepherd@seattlegrace.com', password='pdempsey')
        self.stdout.write(self.style.SUCCESS('Users created successfully'))