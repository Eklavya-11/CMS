from django.db import models

# Create the models.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='menu_images/')
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name