# models.py
from django.db import models
from users.models import User 

class Feedback(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)  # Links feedback to the user who submits it
    rating = models.PositiveIntegerField()  # Positive integer for ratings (1-5)
    comment = models.TextField()  # Text input for the comment
    created_at = models.DateTimeField(auto_now_add=True)  # store the creation timestamp

    def __str__(self):
        return f"Rating: {self.rating}, Comment: {self.comment[:20]}"  # Shrt description in the admin panel
