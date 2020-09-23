from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author_id = models.ForeignKey(
        "posts.author",
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )


class Author(models.Model):
    nick = models.CharField(max_length=20)
    email = models.EmailField()
    bio = models.TextField(null=True, blank=True)
