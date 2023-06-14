from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from apps.user.forms import UserSignUpForm, UserLoginForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def landing_page(request):
    """View to display landing page"""

    return render(
        request, 'index.html', {}
    )


def signup(request):
    """View for signup."""
    form = UserSignUpForm()

    if request.method == "POST":
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)

            dj_login(request, user)

            return redirect("home")

    return render(
        request, 'signup.html', {'form': form}
    )


def login(request):
    """View for login."""
    form = UserLoginForm()

    if request.method == "POST":
        print("POST")
        
        form = UserLoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = authenticate(email=email, password=password)

            if user:
                dj_login(request, user)

                return redirect("home")
            else:
                messages.error(request, "Invalid password")

                return redirect("login")
            
    return render(
        request, 'login.html', {'form': form}
    )


@login_required
def home(request):
    """View for home page."""
    return render(
        request, 'home.html', {'user': request.user}
    )
