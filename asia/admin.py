"""Imports"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    Created a class for summernote field which will tell
    the adminPanel which field to use for summernote
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fileds = ('content')

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Comment Admin model to add built in django filters
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """
        approve comment function to set it true default value is false
        """
        queryset.update(approved=True)
