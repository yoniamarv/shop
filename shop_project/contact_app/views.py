from django.shortcuts import render, redirect
from contact_app.models import Contact
from contact_app.forms import ContactForm

def contact_form(request):
	if request.method =='POST':
		Contact.objects.get_or_create(subject=request.POST.get('subject'), text=request.POST.get('text'), email=request.POST.get('email'))
		return redirect('success/')

	return render(request, 'contact_form.html', context={ 'contact_form': ContactForm() })

def success(request):
	return render(request, 'success.html')

