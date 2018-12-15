from django import forms
from shop_app.models import Comment


class CommentForm(forms.ModelForm):
	class Meta:
		model 	= Comment
		fields 	= ['username', 'text']
		Widgests = {
			'username': forms.TextInput(attrs={
				'id': 'comment-username',
				'placeholder': 'username',
				'required': True
			}),
			'text': forms.Textarea(attrs={
				'id': 'comment-text',
				'placeholder': 'Write a comment here...',
				'required': True
			}),
		} 