from django.urls import path

from Blogapp import views

urlpatterns = [
    # path('', views.base, name='base'),
    #  path('index/<int:id>', views.index, name='index'),
     path('', views.index, name='index'),
     path('single/<int:id>', views.get_single_post_detail, name='single_post'),
     # path('category/<int:name>', views.get_category_post_detail, name='category'),
]
