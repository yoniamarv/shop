from django.shortcuts import render, redirect
from profile_app.forms import SignupForm, LoginForm, ProfileForm, UserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout 
from profile_app.models import Profile

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

def logout_view(request):
    logout(request)
    return redirect('/shop_app/')

def profile(request,user_id):
	user = User.objects.get(id=user_id)
	return render(request,'profile.html', context={'user':user})

def edit_profile(request,user_id):
	user = User.objects.get(id=user_id)
	redirect_link = '/profile_app/profile/{}/'.format(user_id)

	if user_id != request.user.id:
		return redirect(redirect_link)

	try:
		profile = Profile.objects.get(user=user)

	except Profile.DoesNotExist:
		profile = Profile.objects.get_or_create(user=user, bio='')[0]

	if request.method == 'POST':
		user.first_name = request.POST.get('first_name')
		user.last_name = request.POST.get('last_name')
		user.email = request.POST.get('email')
		user.save()

		profile.bio = request.POST.get('bio')
		profile.save()

		return redirect(redirect_link)

	user_form = UserForm(initial={
			'first_name': user.first_name,
			'last_name': user.last_name,
			'email': user.email,
		})
	profile_form = ProfileForm(initial={
			'bio': profile.bio
		})
	

	return render(request,'profile-edit.html', context={'profile_form':profile_form, 'user_form':user_form,})

