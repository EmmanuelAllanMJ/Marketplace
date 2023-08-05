from django.urls import path

from .views import details, new

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', details, name='details'),
    path('new/', new, name='new')
]