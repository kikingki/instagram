from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.
def main(request):
    posts = Post.objects
    return render(request, 'myapp/main.html', {'posts':posts})

def write(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.writer = request.user
            form.save()
            return redirect('main')
    else:
        form = PostForm()
        return render(request, 'myapp/write.html', {'form':form})

def update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.writer = request.user
            form.save()
            return redirect('main')
    else:
        form = PostForm(instance=post)
        return render(request, 'myapp/write.html', {'form':form})

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('main')