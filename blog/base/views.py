from django.shortcuts import render, redirect
from .forms import SignupForm

def homepage(request):
    return render(request, 'base/homepage.html')

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

