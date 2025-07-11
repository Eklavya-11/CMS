from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
]