from django.urls import path
from task_app.calculator.views import add_two_numbers

urlpatterns = [
    path('add/', add_two_numbers)
]