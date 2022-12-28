from django.contrib import admin
from .models import Product,Category,Modifier,ModifierGroup,Address,Restaurant,Menu
# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Modifier)
admin.site.register(ModifierGroup)
admin.site.register(Address)
admin.site.register(Restaurant)
admin.site.register(Menu)