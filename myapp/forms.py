from django import forms
from .models import Post, CustomUser, Comment, Hashtag


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['location', 'body', 'image', 'hashtag_field']

class SigninForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']

class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'nickname']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class HashtagForm(forms.ModelForm):
    class Meta:
        model = Hashtag
        fields = ['name']