from django.test import TestCase, Client
from django.urls import reverse
from .models import Doctor
from django.contrib.auth.models import User

''' This code defines a couple of unit tests for the app.'''

class DoctorModelTests(TestCase): # Testing the Doctor database model
    def test_doctor_creation(self):
        """
        Testing that a Doctor object can be created.
        """
        doctor = Doctor.objects.create(username="testuser", email="test@example.com")
        self.assertIsInstance(doctor, Doctor)
    
    # Add more model tests as needed

class ViewsTests(TestCase): 
    def test_login_view(self):
        """
        Testing that the login view returns a 200 OK status code.
        """
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

class LoginTestCase(TestCase): # Testing the login views
    def setUp(self):
        # Creating a test user
        self.username = 'testuser'
        self.password = 'password123'
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_valid_credentials(self):
        # Creating a test client
        client = Client()

        # Attempingt to login with valid credentials
        response = client.post(reverse('login'), {'username': self.username, 'password': self.password})

        # Checking if the user is logged in and redirected to the home dashboard
        self.assertEqual(response.status_code, 302)  # Redirect status code
        self.assertTrue(response.url.endswith(reverse('home_dashboard')))  # Check redirection

    def test_login_invalid_credentials(self):
        # Creating a test client
        client = Client()

        # Attempting to login with invalid credentials
        response = client.post(reverse('login'), {'username': 'invalid_user', 'password': 'invalid_password'})

        # Checking if the user remains on the login page and gets an error message
        self.assertEqual(response.status_code, 200)  # Success status code
        self.assertContains(response, 'Invalid username or password')  # Check error message in response content
