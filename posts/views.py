from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

from posts.models import Post, Author
from posts.forms import ResultForm

def posts_list(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/posts_list.html",
        context={"posts": posts}
    )

def post_details(request,id):
    post = Post.objects.get(id=id)
    return render(
        request=request,
        template_name="posts/post_details.html",
        context={"post": post}
    )

def authors_list(request):
    pass

def author_details(request):
    pass

