# views.py
from django.shortcuts import render, redirect
from .forms import FeedbackForm

def feedback_form(request):
    
    if not request.user.is_authenticated:
        return redirect('register')  

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.customer = request.user  # Assign the logged-in user to the feedback
            feedback.save()  # Save feedback to the database
            return redirect('thank_you') 
    else:
        form = FeedbackForm()  # Initialize the form if it's a GET request
    return render(request, 'feedback/feedback_form.html', {'form': form})

def thank_you(request):
    return render(request, 'feedback/thank_you.html')