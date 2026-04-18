from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import NewPostForm, EditPost

@login_required
def post_form(request):
    if request.method == 'POST':
        form = NewPostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)  
            post.author = request.user     
            post.save()                     
            return redirect('pages:post_detail', pk=post.id)
    
    else:
        form = NewPostForm()

    return render(request, 'pages/post_form.html', {
        "form": form,
    })

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'pages/post_detail.html', {
        'post': post,
    })

def delete(request, pk):
    post = get_object_or_404(Post, pk=pk, author=request.user)
    post.delete()
    return redirect('base:homepage')