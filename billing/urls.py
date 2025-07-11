from django.urls import path
from . import views

urlpatterns = [
    path('bill/<int:order_id>/', views.generate_bill, name='generate_bill'),
]