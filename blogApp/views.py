from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import BlogForm

# Create your views here.


def list_blogs(request):
    blogs = Post.objects.all()
    return render(request, 'blog_list.html', {'blogs': blogs})


def blog_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog_details.html', {'blog': post})


def blog_create(request):
    form = BlogForm()
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'blog_form.html', {'form': form})
