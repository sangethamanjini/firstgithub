from django.urls import path
from . import views  # Import your views

urlpatterns = [
    path('home', views.homepage, name='homepage'),
    path('about/', views.aboutpage, name='about'),
    path('contact/', views.contactpage, name='contact'),
    path('service/', views.servicepage, name='service'),
    path('products/add/', views.productsAdd, name='products_add'),
    path('products/', views.Allproducts, name='all_products'),
    path('products/delete/<int:id>/', views.Deleteproducts, name='product_delete'),  # Fixed the missing views import
    path('products/update/<int:id>/', views.productupdate, name='product_update'),  # Fixed the missing views import
]

