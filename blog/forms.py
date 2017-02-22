from django import forms #import django forms
from .models import Post #import Post from models

class PostForm(forms.ModelForm):

	class Meta: #this class will tell Django which model that we want to use to create the form
		model = Post
		fields = ('title', 'text',)