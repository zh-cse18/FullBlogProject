from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from Blogapp.forms import CreatePost
from .models import Article, Author, Category
from  django.contrib.auth import login, logout ,authenticate

# def index(request, id ):
#     post = Article.objects.filter(pk=id)
#     category = Category.objects.all()
#     return render(request, 'index.html', {'post': post, 'category': category})

def index(request):
    post1 = Article.objects.all()

    search = request.GET.get('q')
    if search:
        post1 = post1.filter(
            Q(title__icontains=search) |
            Q(body__icontains=search)
        )
    paginator = Paginator(post1, 8)  # Show 25 contacts per page
    page = request.GET.get('page')
    post = paginator.get_page(page)
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


def get_category_post_detail(request, name):
    cat = get_object_or_404(Category, name=name)
    post = Article.objects.filter(category_name=cat.id)
    context = {
        "post": post,
    }
    return render(request, "category.html", context)


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


def author(request, name):
    post_author = get_object_or_404(User, username=name)
    auth = get_object_or_404(Author, name=post_author.id)
    post = Article.objects.filter(author_name=auth.id)
    context ={
        'auth': auth,
        'post': post
    }
    return render(request, 'author.html', context)