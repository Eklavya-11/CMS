# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('feedback/', views.feedback_form, name='feedback_form'),  # Route for the feedback form
    path('thank-you/', views.thank_you, name='thank_you'),  # Redirect after successful submission
    # Other routes (for future ig)
]
