from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login_register/', views.login_register_view, name='login_register'),  # This should call login_register_view 
    # DEAD CODE, USING REGISTER.HTML FILE, prevents error gen of login_register.html. To patch
]
