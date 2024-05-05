from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User
from django.db import models
from django.contrib.auth.models import AbstractUser

''' Database models in Django make use of the SQLite framework. Here, there are 2 such instances. One for creating a 
database of the patient's report and the other for creating a database of the permitted doctors (the superusers)'''

class PatientReport(models.Model):
    patient_name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    image_modality = models.CharField(max_length=50)
    image = models.ImageField(upload_to='xray_images/')
    prediction = models.CharField(max_length=100)


class Doctor(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username