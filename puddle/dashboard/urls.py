from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index

app_name = 'dashboard'

urlpatterns = [
    path('', index, name='dashboard')
]
