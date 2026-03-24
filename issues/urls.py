from django.urls import path

from . import views

urlpatterns = [
    path('issues/', views.issues_handler, name='issues_handler'),
    path('reporters/', views.reporters_handler, name='reporters_handler')
]
