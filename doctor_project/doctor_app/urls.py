from doctor_app import views
from django.urls import path
app_name = 'doctor_site'

urlpatterns = [

    path('discharge/', views.discharge, name='relative'),
    path('patient_register/', views.patient, name='other'),
]
