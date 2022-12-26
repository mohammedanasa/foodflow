from django import forms
from .models import Product,Category,ModifierGroup,Modifier

class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Product Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-100px mb-2 ql-container ql-snow form-control','id':'kt_ecommerce_add_product_description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control mb-2','placeholder':'Product Price'}))

    class Meta:
        model = Product
        fields = ['name', 'description', 'price']


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Category Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-200px mb-2 form-control','id':'kt_ecommerce_add_category_description'}))
    class Meta:
        model = Category
        fields = ['name', 'description']

class ModifierGroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Modifier Group Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-200px mb-2 form-control','id':'kt_ecommerce_add_category_description'}))
    class Meta:
        model = ModifierGroup
        fields = ['name', 'description']


class ModifierForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Modifier Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-100px mb-2 ql-container ql-snow form-control','id':'kt_ecommerce_add_product_description'}))
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control mb-2','placeholder':'Product Price'}))

    class Meta:
        model = Modifier
        fields = ['name', 'description', 'price']