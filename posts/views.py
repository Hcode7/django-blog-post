from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage

# Create your views here.


def posts_list(request):
    post_list = Post.published_posts.all()
    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)
    try:
        posts = paginator.page(page_number)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
         
    return render(request, 'pages/index.html', {'posts' : posts})


def post_detail(request, year , month, day, post):
        post = get_object_or_404(Post, slug=post, published__year=year, published__month=month, published__day=day, )
        return render(request, 'pages/post_detail.html', {'post' : post})