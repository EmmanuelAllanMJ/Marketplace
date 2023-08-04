from django.urls import path
from .views import index, contact, signup

app_name = 'core'

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signup, name='signup')
]
