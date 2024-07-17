from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404
from .forms import CommentForm

# Create your views here.


def posts_list(request):
        post_list = Post.published_posts.all()
        paginator = Paginator(post_list, '3')
        page_number = request.GET.get('page', 1)
        try:
                posts = paginator.page(page_number)
        except PageNotAnInteger:
                posts = paginator.page(1)
        except:
                raise Http404('Page Not Found 404')
        return render(request, 'pages/index.html', {'posts' : posts})


def post_detail(request, year , month, day, post):
        post = get_object_or_404(Post, slug=post, published__year=year, published__month=month, published__day=day, )
        # comment = post.comments.filter()
        return render(request, 'pages/post_detail.html', {'post' : post})


def blog_post(request, post_id):
        post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
        comment=None
        if request.method == 'POST':
                form = CommentForm(data=request.POST)
                if form.is_valid():
                        comment = form.save(commit=False)
                        comment.post = post
                        comment.save()
        else:
                form = CommentForm() 
        return render(request, 'pages/blog_form.html', {'post' : post, 'form' : form})