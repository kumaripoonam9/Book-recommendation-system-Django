from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegistrationForm
from django.contrib.auth import login, logout

# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log the user in
            login(request, user)
            return redirect("/")
    else:
        form = RegistrationForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    # print("\nLOGIN\n")
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login
            user = form.get_user()
            login(request, user)
            # print('\nLOGIN SUCCESS\n')
            # print(f"\n{user}\n")
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def logout_view(request):
    # print("\nlogout\n")
    if request.method == 'POST':
        logout(request)
        return redirect('/')
    # return render(request, "")

def profile(request):
    return render(request, "profile.html")