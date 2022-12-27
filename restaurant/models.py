from django.db import models


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


