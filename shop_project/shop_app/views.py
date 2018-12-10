from django.shortcuts import render
from shop_app.models import Product, Customer


def index(request):
  products = Product.objects.all()[:20]
  return render(request, 'index.html', context={ 'products': products })


def product(request, product_id):
  product = Product.objects.get(id=product_id)
  return render(request, 'product.html', context={ 'product': product })

def customers(request):
  customers = Customer.objects.all()[:20]
  return render(request, 'customers.html', context={ 'customers': customers })

def customer(request, customer_id):
	customer = Customer.objects.get(id=customer_id)
	return render(request, 'customer.html', context={ 'customer': customer })