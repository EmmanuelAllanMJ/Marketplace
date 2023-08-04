from django.urls import path

from .views import details

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', details, name='details'),
]