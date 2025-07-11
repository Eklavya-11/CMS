# forms.py
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['rating', 'comment']
        widgets = {
            'rating': forms.HiddenInput(),  # Rating is hidden, updated by JavaScript
            'comment': forms.Textarea(attrs={'placeholder': 'Your comments...'})
        }
