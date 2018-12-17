from django import forms
from shop_app.models import Comment, Question


class CommentForm(forms.ModelForm):
	class Meta:
		model 	= Comment
		fields 	= ['username', 'text']
		Widgets = {
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

class QuestionForm(forms.ModelForm):
	class Meta:
		model 	= Question
		fields 	= ['title', 'text', 'username']
		Widgets = {
			'title': forms.TextInput(attrs={
				'id': 'question-title',
				'placeholder': 'title',
				'required': True
			}),
			'text': forms.Textarea(attrs={
				'id': 'question-text',
				'placeholder': 'Quelle est votre question...',
				'required': True
			}),
			'username': forms.TextInput(attrs={
				'id': 'question-username',
				'placeholder': 'username',
				'required': True
			}),
		} 
		

