
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Doctor

''' When a superuser is created, this form gets called. The admin gets to enter the username and password. 
The password must be entered twice and it needs to match both times for it to be accpeted. The prompt 
raises an alert if the password is less than 8 characters or is too common. However, to allow for easy 
use of this project, there is an option to override the alert and use the password of interest. '''

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Doctor
        fields = ['username', 'password1', 'password2']

''' This form is used to generate reports of the diagnosis. After the doctor passes the image through the model, 
the results are produced. The doctor then has the option to generate a report with the model's prediction by 
filling out the entries below. '''

class ReportForm(forms.Form):
    patient_name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    image_modality = forms.CharField(max_length=50)
    image = forms.FileField()
    prediction = forms.CharField(max_length=50)