from django.db import models
from datetime import date

class Post(models.Model):
    """A post I'll create"""
    title=models.CharField(max_length=30)
    text=models.TextField()
    date_added = models.DateField(default=date.today)
