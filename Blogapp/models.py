from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    details = models.TextField()
    profile_pic = models.FileField()

    def __str__(self):
        return self.name.username


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Article(models.Model):
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.FileField()
    posted_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    post_update = models.DateTimeField(auto_now=True, auto_now_add=False)
    body = models.TextField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " hello"

    def __str__(self):
        if len(self.body) > 50:
            return self.body[:20] + "...."
        return self.body + "Zahid "
