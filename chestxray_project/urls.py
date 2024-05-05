from django.contrib import admin
from django.urls import path
from chestxray import views
from django.urls import path, include
from chestxray.views import login_view
from django.contrib.auth import views as auth_views

''' This code contains all the  URLs needed for the project. Each page is defined by a unique URL for redirection. 
The redirection is controlled by views.py '''

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home-dashboard/', views.home_dashboard, name='home_dashboard'),
    path('xray-analyzer/', views.xray_analyzer, name='xray_analyzer'),
    path('report-generator/', views.generate_report, name='generate_report'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', auth_views.LoginView.as_view(), name='login'),  # Opening URL
]

