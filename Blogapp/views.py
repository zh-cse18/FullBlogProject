from django.shortcuts import render, get_object_or_404, redirect
from Blogapp.forms import CreatePost
from .models import Article, Author, Category
from  django.contrib.auth import login, logout ,authenticate

# def index(request, id ):
#     post = Article.objects.filter(pk=id)
#     category = Category.objects.all()
#     return render(request, 'index.html', {'post': post, 'category': category})

def index(request):
    post = Article.objects.all()
    return render(request, 'index.html', {'post': post})


def get_single_post_detail(request, id):
    post = get_object_or_404(Article, pk=id)
    author = get_object_or_404(Article, pk=id)
    first = Article.objects.first()
    last = Article.objects.last()
    related = Article.objects.filter(category_name=post.category_name).exclude(id=id)[:4]

    context = {
        'author': author,
        "post": post,
        "first": first,
        "last": last,
        'related': related

    }
    return render(request, "single.html", context)


# def get_category_post_detail(request, name):
#     cat = get_object_or_404(Category, name=name)
#     post = Article.objects.filter(category_name=cat.id)
#     context = {
#         "post": post,
#     }
#     return render(request, "category.html", context)


def create_post(request):
    form = CreatePost(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return redirect('index')
    return render(request, 'create_post.html', {'form': form})


def login_user(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST.get('user')
            password = request.POST.get('password')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('index')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return redirect('index')