from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import BlogForm

# Create your views here.


def list_blogs(request):
    blogs = Post.objects.all()
    sort = request.GET.get('sort')
    if sort == 'newest':
        blogs = blogs.order_by('-created_at')
    elif sort == 'oldest':
        blogs = blogs.order_by('created_at')
    elif sort == 'updated':
        blogs = blogs.order_by('-updated_at')
    else:
        blogs = blogs.order_by('-created_at')
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


def update_blog(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            redirect('/')
    else:
        form = BlogForm(instance=post)
    return render(request, 'blog_form.html', {'form': form})


def remove_post(request, pk):
    blog = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
