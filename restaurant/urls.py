from django.urls import path
from .views import ProductList,ProductCreate,ProductUpdate,ProductDelete,CategoryCreate,CategoryList,CategoryUpdate,CategoryDelete,MGCreate,MGList,MGUpdate,MGDelete,ModifierList,ModifierCreate,ModifierDelete,ModifierUpdate
urlpatterns = [

    path('products/', ProductList.as_view(), name='products'),
    path('products/create-product', ProductCreate.as_view(), name='create-product'),
    path('products/update-product/<int:pk>/', ProductUpdate.as_view(), name='update-product'),
    path('products/delete-product/<int:pk>/', ProductDelete.as_view(), name='delete-product'),

    path('categories/', CategoryList.as_view(), name='categories'),
    path('categories/create-category', CategoryCreate.as_view(), name='create-category'),
    path('categories/update-category/<int:pk>/', CategoryUpdate.as_view(), name='update-category'),
    path('categories/delete-category/<int:pk>/', CategoryDelete.as_view(), name='delete-category'),

    path('modifier-groups/', MGList.as_view(), name='modifiergroups'),
    path('modifier-groups/create-modifier-group', MGCreate.as_view(), name='create-mg'),
    path('modifier-groups/update-modifier-group/<int:pk>/', MGUpdate.as_view(), name='update-mg'),
    path('modifier-groups/delete-modifier-groups/<int:pk>/', MGDelete.as_view(), name='delete-mg'),

    path('modifiers/', ModifierList.as_view(), name='modifiers'),
    path('modifiers/create-modifier', ModifierCreate.as_view(), name='create-modifier'),
    path('modifiers/update-modifier/<int:pk>/', ModifierUpdate.as_view(), name='update-modifier'),
    path('modifiers/delete-modifier/<int:pk>/', ModifierDelete.as_view(), name='delete-modifier'),
]
