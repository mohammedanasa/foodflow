from django.contrib import admin
from .models import Product,Category,Modifier,ModifierGroup
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Modifier)
admin.site.register(ModifierGroup)