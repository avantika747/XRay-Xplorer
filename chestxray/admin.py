from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Doctor

# Creating the admin of the app chestxray

class DoctorAdmin(admin.ModelAdmin):
    model = Doctor
    list_display = ('email', 'username')
    search_fields = ('email', 'username')

admin.site.register(Doctor, DoctorAdmin)