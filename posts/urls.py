from django.contrib import admin
from django.urls import path
from posts.views import posts_list, post_details, authors_list, author_details, homepage

app_name = "posts"
urlpatterns = [
    path('', homepage),
    path('posts/', posts_list, name="posts_list"),
    path('posts/<int:id>', post_details, name="post_details"),
    path('authors/', authors_list, name="authors_list"),
    path('authors/<int:id>', author_details, name="author_details"),
]
