from django.shortcuts import render
from .models import Post

# Create your views here.


def list_blogs(request):
    blogs = Post.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})
