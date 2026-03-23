from django.shortcuts import render, redirect
from pages.models import Post
from .forms import SignupForm

def homepage(request):
    posts = Post.objects.all()
    return render(request, 'base/homepage.html',{
        'posts':posts,
    })

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()
            user.profile.save()

            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'base/sign-up.html', {
        "form":form,
    })

def login(request):
    return render(request, 'base/login.html')

