from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=50)
    details=models.CharField(max_length=100)
    cost=models.IntegerField()
    
