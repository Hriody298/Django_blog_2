from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User,Article,Author,Comment


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2'
        ]


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title',
            'image',
            'body'
        ]


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name',
            'profile_picture',
            'detail',
            'category'
        ]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'body'
        ]