from django.shortcuts import render, get_object_or_404
from .models import Article, Author, Category


# def index(request, id ):
#     post = Article.objects.filter(pk=id)
#     category = Category.objects.all()
#     return render(request, 'index.html', {'post': post, 'category': category})

def index(request):
    post = Article.objects.all()
    category = Article.objects.filter(category_name=4)
    return render(request, 'index.html', {'post': post, 'category': category})


def get_single_post_detail(request, id):
    post = get_object_or_404(Article, pk=id)
    author = get_object_or_404(Article, pk=id)
    first = Article.objects.first()
    last = Article.objects.last()

    context = {
        'author': author,
        "post": post,
        "first": first,
        "last": last,

    }
    return render(request, "single.html", context)


# def get_category_post_detail(request, cat):
#     post = Article.objects.filter(category_name=cat)
#     context = {
#         "post": post,
#     }
#     return render(request, "category.html", context)