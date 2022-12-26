from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Product Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-100px mb-2 ql-container ql-snow form-control','id':'kt_ecommerce_add_product_description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control mb-2','placeholder':'Product Price'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']