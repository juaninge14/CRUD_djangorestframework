from django.db import models

# Create your models here.

class Project(models.Model):
    Title = models.CharField(max_length=100)
    Description = models.TextField()
    Technology = models.CharField(max_length=150)
    Created_at = models.DateTimeField(auto_now_add=True)