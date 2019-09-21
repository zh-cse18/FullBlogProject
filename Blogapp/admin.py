from django.contrib import admin
from django.contrib.admin import site

from Blogapp.models import Author, Category, Article


class ArticleAdmin(admin.ModelAdmin):

     list_display = ['author_name', 'title', 'body', 'category_name', 'posted_on', 'post_update']
     search_fields = ['body', 'title']
     list_filter = ['posted_on', 'author_name']


admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

