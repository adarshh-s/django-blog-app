from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.


def list_blogs(request):
    blogs = Post.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_details.html', {'blog': post})
