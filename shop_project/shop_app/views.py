from django.shortcuts import render, redirect
from shop_app.models import Product, Customer, Comment, Maillot, Question, Response, CommentResponse
from shop_app.forms import CommentForm, QuestionForm, ResponseForm, CommentResponseForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
import datetime
import logging


def search(request,value):
	products = Product.objects.all().filter(name = value)
	return render(request, 'index.html', context={'products': products})

def index(request):
	users = User.objects.all().filter(is_superuser=False)
	user = None
	
	if request.user.is_authenticated:
		  user = request.user
	products = Product.objects.all()
	return render(request, 'index.html', context={ 'products': products, 'user': user})
	
def product(request, product_id):
	logging.info('debug logged')
	product = Product.objects.get(id=product_id)
	comments = Comment.objects.all().filter(product_id=product_id).order_by('-date')[:20]
	questions = Question.objects.all().filter(product_id=product_id)
	
	comments_with_responses = []
	for comment in comments:
		comment_with_responses = {
  		 'comment': comment,
      	 'comment_responses': CommentResponse.objects.all().filter(comment_id=comment.id)
    	}
		comments_with_responses.append(comment_with_responses)

	questions_with_responses = []
	for question in questions:
		question_with_responses = {
	      'question': question,
	      'responses': Response.objects.all().filter(question_id=question.id)
	    }
		questions_with_responses.append(question_with_responses)	
	
	return render(request, 'product.html', context={
      'product': product,
      'comments': comments_with_responses,
      'questions': questions_with_responses,
    })


def customers(request):
	customers = Customer.objects.all()[:20]
	return render(request, 'customers.html', context={ 'customers': customers })

def customer(request, customer_id):
	customer = Customer.objects.get(id=customer_id)
	return render(request, 'customer.html', context={ 'customer': customer })

def maillots(request):
	maillots = Maillot.objects.all()[:20]
	return render(request, 'maillots.html', context={ 'maillots': maillots })

def maillot(request, maillot):
	maillot = Maillot.objects.get(id=maillot)
	return render(request, 'maillot.html', context={ 'maillot': maillot })

def comment_form(request, product_id):
  redirect_to_product_link = '/shop_app/products/{}'.format(product_id)

  if not request.user.is_authenticated:
    return redirect(redirect_to_product_link)

  if request.method == 'POST':
    Comment.objects.get_or_create(
      user=request.user,
      text=request.POST.get('text'),
      date=datetime.datetime.now(),
      product=Product.objects.get(id=product_id)
    )

    return redirect(redirect_to_product_link)

  return render(request, 'comment_form.html', context={ 'comment_form': CommentForm() })

def question_form(request, product_id):
	if request.method =='POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		product = Product.objects.get(id=product_id)
		title = request.POST.get('title')
		questions = Question.objects.get_or_create(username=username, text=text, product=product, title=title)
		return redirect(redirect_to_product_link)

	return render(request, 'question_form.html', context={ 'question_form': QuestionForm() })

def response_form(request, question_id):
	if request.method =='POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		question = Question.objects.get(id=question_id)
		Response.objects.get_or_create(username=username, text=text, question=question)
		return redirect(redirect_to_product_link)
		
	return render(request, 'response_form.html', context={ 'response_form': ResponseForm() })

def comment_response_form(request, comment_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		comment = Comment.objects.get(id=comment_id)
		CommentResponse.objects.get_or_create(username=username, text=text, comment=comment)
		return redirect( '/shop_app/products/{}'.format(comment.product.id) )

	return render(request, 'comment_response_form.html', context={ 'comment_response_form': CommentResponseForm() })