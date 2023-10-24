from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import UserCreationForm, LoginForm
from django.contrib import messages

showResults = False

# Create your views here.
# Home page
def home(request, template_name='index.html'):
    return render(request, template_name)

class user:
    # signup page
    def signup(request):
        if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        else:
            form = UserCreationForm()
        print(form)
        return render(request, 'signup.html', {'form': form})

        # login page
    def authenticate(request):
        messages.success(request, 'You have been successfully logged in.')   
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user:
                    login(request, user) 
                    return redirect('home')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})

# logout page
def user_logout(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('home')

def upload():
    showResults = True
    return redirect('home')