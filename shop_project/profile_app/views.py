from django.shortcuts import render, redirect
from profile_app.forms import SignupForm, LoginForm, ProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout 

# Create your views here.


def signup(request):

	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name)
		user = authenticate(request,username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('/shop_app/')


	return render(request,'signup.html', context={'signup_form': SignupForm()})

def login_auth(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('/shop_app/')
		

	return render(request,'login.html', context={'login_form': LoginForm()})

def profile(request,user_id):
	user = User.objects.get(id=user_id)
	return render(request,'profile.html', context={'user':user})

def edit_profile(request,user_id):
	user = User.objects.get(id=user_id)
	redirect_link = '/profile_app/profile/{}/'.format(user_id)
	if user_id != request.user.id:
		return redirect(redirect_link)

	if request.method == 'POST':
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.save()
		return redirect(redirect_link)
	profile_form = ProfileForm(initial={'first_name':user.first_name,'last_name':user.last_name})

	return render(request,'profile-edit.html', context={'profile_form':profile_form})

def logout_view(request):
    logout(request)
    return redirect('/shop_app/')

