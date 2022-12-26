from django.urls import path
from .views import ProductList,ProductDetail,ProductCreate,ProductUpdate,ProductDelete

urlpatterns = [

    path('products/', ProductList.as_view(), name='products'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product'),
    path('products/create-product', ProductCreate.as_view(), name='create-product'),
    path('products/update-product/<int:pk>/', ProductUpdate.as_view(), name='update-product'),
    path('products/delete-product/<int:pk>/', ProductDelete.as_view(), name='delete-product'),
]
