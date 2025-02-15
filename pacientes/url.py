from django.urls import path
from . import views

urlpatterns = [
    path('teste/', views.pacientes, name="pacientes"),
]