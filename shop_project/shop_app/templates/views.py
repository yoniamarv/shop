register = False
if request.method =='POST':
    user_form = forms.UserForm(data= request.POST)
    profile_form = forms.UserProfileIntoForm(data= request.POST)

    if user_form.is_valid() and profile_form.is_valide():
        user = user_form.save()
        user.set_password(user.password)
        user.save()

        profile = profile_from.save(commit= False)
        profile.user = user

        if 'profile_pics' in request.FILES:
            profile.profile_pic = request.FILES['profile_pics']
        
        profile.save()
        registered = True
        login(request, user)
        return register('/first_app/home/', permanent=False)

    else:
        print(user_form.error, profile_form.error)

    