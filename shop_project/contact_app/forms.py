from django import forms
from shop_app.models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model 	= Contact
		fields 	= ['subject', 'email', 'text']
		Widgets = {
			'subject': forms.TextInput(attrs={
				'id': 'Contact-subject',
				'placeholder': 'subject',
				'required': True
				}),
			'email': forms.EmailInput(attrs={
				'id': 'contact-email',
				'placeholder': 'email',
				'required': True
				}),
			'text': forms.Textarea(attrs={
				'id': 'ccontact-text',
				'placeholder': 'Write a contact here...',
				'required': True
				})
		} 