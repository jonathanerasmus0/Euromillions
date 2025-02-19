from django.urls import path
from .views import index, generate_numbers

urlpatterns = [
    path('', index, name='index'),
    path('generate/', generate_numbers, name='generate_numbers'),
]
