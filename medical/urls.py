"""medical URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from base import views as base_views

urlpatterns = [
    path('', LoginView.as_view(template_name='login.html'), name='login'),
    path('main/', include('main.urls')),
    path('base/', include('base.urls')),
	path('clients/', include('clients.urls')),
    path('admin/', admin.site.urls),
]
