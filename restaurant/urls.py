from django.urls import path
from .views import ProductList,ProductCreate,ProductUpdate,ProductDelete,CategoryCreate,CategoryList,CategoryUpdate,CategoryDelete

urlpatterns = [

    path('products/', ProductList.as_view(), name='products'),
    path('products/create-product', ProductCreate.as_view(), name='create-product'),
    path('products/update-product/<int:pk>/', ProductUpdate.as_view(), name='update-product'),
    path('products/delete-product/<int:pk>/', ProductDelete.as_view(), name='delete-product'),

    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/create-category', CategoryCreate.as_view(), name='create-category'),
    path('categories/update-category/<int:pk>/', CategoryUpdate.as_view(), name='update-category'),
    path('categories/delete-category/<int:pk>/', CategoryDelete.as_view(), name='delete-category'),
]
