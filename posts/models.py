from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        "posts.Author",
        on_delete=models.CASCADE,
    )


class Author(models.Model):
    nick = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)
