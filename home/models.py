from django.db import models
from django.contrib.auth.models import User
import base64

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image_base64 = models.TextField(null=True, blank=True)  # Store base64 string
    recipe_views_count = models.IntegerField(default=1)

    def save_base64_image(self, image_file):
        if image_file:
            # Convert image file to base64 string
            image_data = image_file.read()
            image_base64 = base64.b64encode(image_data).decode('utf-8')
            self.recipe_image_base64 = image_base64
