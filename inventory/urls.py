from django.urls import path
from . import views

urlpatterns = [
    path('report/', views.inventory_report, name='inventory_report'),
]