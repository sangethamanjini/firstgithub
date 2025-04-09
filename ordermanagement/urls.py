from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),  # Home page
    path('about/', views.aboutpage, name='about'),  # About page
    path('contact/', views.contactpage, name='contact'),  # Contact page
    path('services/', views.servicepage, name='services'),  # Services page
    
    # Customer-related URLs
    path('customers/add/', views.customerAdd, name='customer_add'),  # Add customer
    path('customers/', views.all_customers_view, name='all_customer'),  # View all customers
    path('customers/update/<int:pk>/', views.customerUpdate, name='customer_update'),  # Update customer
    path('customers/delete/<int:pk>/', views.customerDelete, name='customer_delete'),  # Delete customer
]
