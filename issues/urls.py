from django.urls import path

from . import views

urlpatterns = [
    path('issues/', views.issues_handler, name='issues_handler')
]
