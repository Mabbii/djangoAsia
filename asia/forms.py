"""Imports"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """Form for adding comments to the blogs"""
    class Meta:
        """Meta Class"""
        model = Comment
        fields = ('body',)
