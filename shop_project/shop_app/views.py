from django.shortcuts import render
from shop_app.models import Product, Customer, Comment, Maillot 
from shop_app.forms import CommentForm
import datetime


def index(request):
	products = Product.objects.all()[:20]
	return render(request, 'index.html', context={ 'products': products })


def product(request, product_id):
	product = Product.objects.get(id=product_id)
	comments = Comment.objects.filter(product_id=product.id)
	return render(request, 'product.html', context={'product': product, 'comments': comments })

def customers(request):
	customers = Customer.objects.all()[:20]
	return render(request, 'customers.html', context={ 'customers': customers })

def customer(request, customer_id):
	customer = Customer.objects.get(id=customer_id)
	return render(request, 'customer.html', context={ 'customer': customer })

def maillots(request):
	customers = Customer.objects.all()[:20]
	return render(request, 'maillots.html', context={ 'maillots': maillots })

def maillot(request, maillot):
	maillot = Maillot.objects.get(id=maillot)
	return render(request, 'maillot.html', context={ 'maillot': maillot })

def comment_form(request, product_id):
	if request.method =='POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		product = Product.objects.get(id= product_id)
		date = datetime.datetime.now()
		comment = Comment.objects.get_or_create(username=username, text=text, product=product, date=date)

	return render(request, 'comment_form.html', context={ 'comment_form': CommentForm() })

