from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=260,null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=260,null=True, blank=True)
    
    def __str__(self):
        return self.name
