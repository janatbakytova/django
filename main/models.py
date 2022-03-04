from email import contentmanager
from pydoc import describe
from unicodedata import name
from django.db import models

# Create your models here.

class ToDoListItem(models.Model):
    content = models.TextField()

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    created  = models.DateTimeField(auto_now_add=True)
    
