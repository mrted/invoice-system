from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=300, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=20)
    tel = models.CharField(max_length=14)
    email = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Invoice(models.Model):
    title = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=300, null=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title