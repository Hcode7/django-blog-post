from django.contrib import admin
from .models import Post, Comment

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'slug', 'published', 'status']
    list_filter = ['status', 'created_at', 'published', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug' : ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'published'
    ordering = ['status', 'published']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = [
        'post' , 'name' , 'body' , 'created_at', 'email', 'created_at'
    ]
    list_filter = ['active', 'created_at', 'updated_at']
    search_fields = ['name' , 'email' , 'body']