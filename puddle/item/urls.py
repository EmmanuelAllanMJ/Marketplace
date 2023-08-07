from django.urls import path

from .views import details, new, delete, items

app_name = 'item'

urlpatterns = [
    path('', items, name='items'),
    path('<int:pk>/', details, name='details'),
    path('new/', new, name='new'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('edit/<int:pk>/', new, name='edit'),
]