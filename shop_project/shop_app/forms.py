from django import forms
from django.contrib.auth.models import User
from shop_app.models import Comment, Question, Response, CommentResponse


class CommentForm(forms.ModelForm):
	class Meta:
		model 	= Comment
		fields 	= ['text']
		Widgets = {
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

class ResponseForm(forms.ModelForm):
	class Meta:
		model 	= Response
		fields 	= ['username', 'text']
		Widgets = {
			'username': forms.TextInput(attrs={
				'id': 'response-username',
				'placeholder': 'username',
				'required': True
			}),
			'text': forms.Textarea(attrs={
				'id': 'response-text',
				'placeholder': 'Quelle est votre reponse...',
				'required': True
			}),
			
		}

class CommentResponseForm(forms.ModelForm):
	class Meta:
		model 	= CommentResponse
		fields 	= ['username', 'text']
		Widgets = {
			'username': forms.TextInput(attrs={
				'id': 'comment-response-username',
				'placeholder': 'username',
				'required': True
			}),
			'text': forms.Textarea(attrs={
				'id': 'comment-response-text',
				'placeholder': 'Laisse un commentaire sur cette reponse...',
				'required': True
			}),
			
		}


		


