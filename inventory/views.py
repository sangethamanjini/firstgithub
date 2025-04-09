from django.shortcuts import render,redirect
from .forms import ProductForm  # Import the ProductForm
from .models import Product  # Import the Product model

def homepage(request):
    data = {
        "name": "Muthu Raja",
        "role": "admin",
        "numbers": [1, 2, 3, 4, 5],
        "marks": {
            "tamil": 100,
            "english": 99
        }
    }
    return render(request, 'home.html', data)

def aboutpage(request):
    return render(request, 'about.html')

def contactpage(request):
    return render(request, 'contact.html')

def servicepage(request):
    return render(request, 'service.html')

def productsAdd(request):
    context = {
        'product_form': ProductForm()  # Initialize the ProductForm
    }

    if request.method == "POST":
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product_form.save()  # Save the product
            return redirect('all_products')  # Redirect to the list of products

    return render(request, 'products_add.html', context)

def Allproducts(request):
    context = {
        "all_products": Product.objects.all()  # Fetch all products
    }
    return render(request, 'products.html', context)

def Deleteproducts(request, id):
    try:
        
        selected_product = Product.objects.get(id=id)
        
        selected_product.delete()
        
    except Product.DoesNotExist:
        
        return redirect('/inventory/products/', {'error': 'Product not found'})

    
    return redirect('/inventory/products/')

def productupdate(request, id):
    try:
        
        selected_product = Product.objects.get(id=id)
    except Product.DoesNotExist:
       
        return redirect('/inventory/products/', {'error': 'Product not found'})

    
    if request.method == "POST":
        product_form = ProductForm(request.POST, instance=selected_product)
        if product_form.is_valid():
            product_form.save()
            return redirect('/inventory/products/')  

    # If the request is GET, display the form with the existing product data
    context = {
        "product_form": ProductForm(instance=selected_product)
    }

    return render(request, 'products_add.html', context)

