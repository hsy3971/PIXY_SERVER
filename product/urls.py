from django.urls import path
from .views import ProductList,ProductDetail,SalesList,SalesDetail, product_list_by_date

urlpatterns = [
     path('product/',ProductList, name='product-list'),
     path('product/<int:pk>/',ProductDetail, name='product-detail'),
     path('product-by-date/', product_list_by_date, name='product-list-by-date'),
     path('sales/', SalesList, name='sales-list'),
     path('sales/<int:pk>/', SalesDetail, name='sales-detail'),
  
]
   