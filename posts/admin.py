from django.contrib import admin
from posts.models import Post, Author


@admin.register(Post)
class ResultAdmin(admin.ModelAdmin):
   list_display = ['author', 'title', 'content', 'created', 'modified']
   list_filter = ['author', 'created', 'modified']
   search_fields = ['author_id__nick', 'title']
@admin.register(Author)
class ResultAdmin(admin.ModelAdmin):
   list_display = ['nick', 'email']
   search_fields = ['nick', 'email']
   list_filter = ['nick', 'email']