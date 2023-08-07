from django.urls import path

from .views import  new, delete, items, details, newItem

app_name = 'item'

urlpatterns = [
    path('', items, name='items'),
    path('new/', new, name='new'),
    path('<int:pk>/', details, name='details'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('edit/<int:pk>/', newItem, name='edit'),
]