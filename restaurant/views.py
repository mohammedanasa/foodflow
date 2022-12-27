from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Product,Category,ModifierGroup,Modifier
from .forms import ProductForm,CategoryForm,ModifierGroupForm,ModifierForm

#UserAuthentication
def login_user(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('products')
		else:
			messages.success(request, ("Your username/password is incorrect."))	
			return redirect('login')	


	else:
		return render(request, 'restaurant/sign-in.html', {})


#Product Views
class ProductList(LoginRequiredMixin,ListView):
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
class ProductCreate(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm 
    success_url = reverse_lazy('products')
class ProductUpdate(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm 
    success_url = reverse_lazy('products')
class ProductDelete(LoginRequiredMixin, DeleteView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy('products')
    template_name = 'restaurant/delete_product.html'

#Category Views
class CategoryList(LoginRequiredMixin,ListView):
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class CategoryCreate(LoginRequiredMixin, CreateView):
    model = Category
    form_class = CategoryForm 
    success_url = reverse_lazy('categories')

class CategoryUpdate(LoginRequiredMixin, UpdateView):
    model = Category
    form_class = CategoryForm 
    success_url = reverse_lazy('categories')

class CategoryDelete(LoginRequiredMixin, DeleteView):
    model = Category
    fields = '__all__'
    success_url = reverse_lazy('Categories')
    template_name = 'restaurant/delete_category.html'

#ModifierGroup Views
class MGList(LoginRequiredMixin,ListView):
    model = ModifierGroup
    context_object_name = 'modifiergroups'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class MGCreate(LoginRequiredMixin, CreateView):
    model = ModifierGroup
    form_class = ModifierGroupForm 
    success_url = reverse_lazy('modifiergroups')

class MGUpdate(LoginRequiredMixin, UpdateView):
    model = ModifierGroup
    form_class = ModifierGroupForm 
    success_url = reverse_lazy('modifiergroups')

class MGDelete(LoginRequiredMixin, DeleteView):
    model = ModifierGroup
    fields = '__all__'
    success_url = reverse_lazy('modifiergroups')
    template_name = 'restaurant/delete_modifiergroup.html'

#Modifiers Views
class ModifierList(LoginRequiredMixin,ListView):
    model = Modifier
    context_object_name = 'modifiers'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ModifierCreate(LoginRequiredMixin, CreateView):
    model = Modifier
    form_class = ModifierForm 
    success_url = reverse_lazy('modifiers')

class ModifierUpdate(LoginRequiredMixin, UpdateView):
    model = Modifier
    form_class = ModifierForm 
    success_url = reverse_lazy('modifiers')

class ModifierDelete(LoginRequiredMixin, DeleteView):
    model = Modifier
    fields = '__all__'
    success_url = reverse_lazy('modifiers')
    template_name = 'restaurant/delete_modifier.html'






