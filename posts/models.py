from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique_for_date='published')
    body = models.TextField()
    published = models.DateTimeField(default=timezone.now())
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class PublishManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=Post.Status.PUBLISHED)

    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    objects  = models.Manager()
    published_posts = PublishManager()


    class Meta:
        ordering = ['-published']
        indexes = [
            models.Index(fields=['-published'])
        ]

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={
            'year': self.published.year,
            'month': self.published.month,
            'day': self.published.day,
            'post': self.slug,
        })
    def __str__(self):
        return self.title
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    name = models.CharField(max_length=255)
    body = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created_at']
        indexes = [
            models.Index(fields=['created_at'])
        ]

    def __str__(self):
        return f'this comment by {self.name} on {self.post}'