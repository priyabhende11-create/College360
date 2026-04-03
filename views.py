from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import LoginAttempt
from .forms import PrincipalLoginForm

def principal_login(request):
    if request.method == "POST":
        form = PrincipalLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user using Django's built-in User model
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Login the user
                # Save login attempt
                LoginAttempt.objects.create(username=username, role="principal")
                return redirect("principal_dashboard")
            else:
                error = "Invalid username or password"
                return render(request, "principal_login.html", {"form": form, "error": error})
    else:
        form = PrincipalLoginForm()
    return render(request, "principal_login.html", {"form": form})

def principal_dashboard(request):
    return render(request, "principal_dashboard.html")
