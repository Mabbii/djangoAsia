"""Imports"""
from django import forms
from .models import Comment, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'author',
            'featured_image',
            'content',
            'status'
            )



class CommentForm(forms.ModelForm):
    """Form for adding comments to the blogs"""
    class Meta:
        """Meta Class"""
        model = Comment
        fields = ('body',)
