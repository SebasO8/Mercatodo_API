from django.urls import path
from .views import ProductsView
from .views import CategoriesView
from .views import ProviderView

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products_list'),
    path('products/<int:prod_id>', ProductsView.as_view(), name='product'),
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('providers/', ProviderView.as_view(), name='providers'),
]