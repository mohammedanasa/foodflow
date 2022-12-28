from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    firstaddress = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.street


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=260,null=True, blank=True)
    image = models.ImageField(upload_to='categories/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Modifier(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=260,null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='modifiers/', null=True, blank=True)

    def __str__(self):
        return self.name

class CustomerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True)
    

class ModifierGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=260,null=True, blank=True)
    modifier = models.ManyToManyField(Modifier, blank=True, null=True)
    image = models.ImageField(upload_to='modifiergroups/', null=True, blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=260,null=True, blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, null=True)
    modifiergroup = models.ManyToManyField(ModifierGroup, blank=True, null=True)
    
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    locationid = models.CharField(max_length=100)
    description = models.TextField(max_length=250,null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250,null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, null=True)
    product = models.ManyToManyField(Product, blank=True, null=True)
    

    def __str__(self):
        return self.name


