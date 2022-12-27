from django import forms
from .models import Product,Category,ModifierGroup,Modifier


class CategoryModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ModifierModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name

class ModifierGroupModelMultipleChoiceField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class ProductForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Product Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-100px mb-2 ql-container ql-snow form-control'}),required=False)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control mb-2','placeholder':'Product Price'}))
    category = CategoryModelMultipleChoiceField(
        queryset=Category.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select mb-2', 'data-placeholder':'Select an option','data-control':'select2'}),
        required=False
    )
    modifiergroup = ModifierGroupModelMultipleChoiceField(
        queryset=ModifierGroup.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select mb-2', 'data-placeholder':'Select an option','data-control':'select2'}),
        required=False
    )
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'type':'file','accept':".png, .jpg, .jpeg"}),required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price','category','modifiergroup','image']


class CategoryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Category Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-200px mb-2 form-control','id':'kt_ecommerce_add_category_description'}),required=False)
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'type':'file','accept':".png, .jpg, .jpeg"}),required=False)
    class Meta:
        model = Category
        fields = ['name', 'description','image']

class ModifierGroupForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Modifier Group Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-200px mb-2 form-control','id':'kt_ecommerce_add_category_description'}),required=False)
    modifier = ModifierModelMultipleChoiceField(
        queryset=Modifier.objects.all(),
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'form-check form-check-inline mb-2','id':'inlineCheckbox1','type':'checkbox'}),
        required=True,
    )
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'type':'file','accept':".png, .jpg, .jpeg"}),required=False)
    class Meta:
        model = ModifierGroup
        fields = ['name', 'description','modifier','image']


class ModifierForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-2','placeholder':'Modifier Name'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'min-h-100px mb-2 ql-container ql-snow form-control','id':'kt_ecommerce_add_product_description'}),required=False)
    price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control mb-2','placeholder':'Modifier Price'}))
    modifiergroup = ModifierGroupModelMultipleChoiceField(
        queryset=ModifierGroup.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select mb-2', 'data-placeholder':'Select an option','data-control':'select2'}),
        required=False
    )
    image = forms.FileField(widget=forms.ClearableFileInput(attrs={'type':'file','accept':".png, .jpg, .jpeg"}),required=False)

    class Meta:
        model = Modifier
        fields = ['name', 'description', 'price','image','modifiergroup']