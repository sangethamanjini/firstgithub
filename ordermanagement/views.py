from django.shortcuts import render, redirect, get_object_or_404
from .form import CustomerForm  # Ensure the form class is named correctly
from .models import Customer  # Ensure the model class is named correctly

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

def customerAdd(request):
    # Adding a new customer
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)  # Correct form class reference
        if customer_form.is_valid():
            customer_form.save()
            return redirect('all_customer')  # Assuming 'all_customer' is a valid URL name
    else:
        customer_form = CustomerForm()  # Correct form initialization

    context = {
        'customer_form': customer_form
    }
    return render(request, 'customer_add.html', context)

def all_customers_view(request):
    # Fetch all customer records from the database
    all_customers = Customer.objects.all()
    
    # Pass the customers to the template
    context = {
        'all_customers': all_customers
    }
    return render(request, 'customer.html', context)

def customerUpdate(request, pk):
    # Updating an existing customer
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer_form = CustomerForm(request.POST, instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            return redirect('all_customer')
    else:
        customer_form = CustomerForm(instance=customer)

    context = {
        'customer_form': customer_form,
        'customer': customer
    }
    return render(request, 'customer_add.html', context)

def customerDelete(request, pk):
    # Deleting an existing customer
    customer = get_object_or_404(Customer, pk=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('all_customer')

    context = {
        'customer': customer
    }
    return render(request, 'customer_add.html', context)
