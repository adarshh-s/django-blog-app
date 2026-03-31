from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_blogs, name='blog_list'),
    path('/blog-detail/<int:pk>', views.blog_detail, name='blog_detail'),
    path('/create-blog', views.blog_create, name='blog_create'),
]
