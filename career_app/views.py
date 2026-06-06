from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'career_app/home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()

    return render(request, 'career_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_superuser:
                return redirect('super_admin_dashboard')
            elif user.is_staff:
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'career_app/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@login_required
def dashboard_view(request):
    return render(request, 'career_app/dashboard.html')


@login_required
def admin_dashboard_view(request):
    if not request.user.is_staff:
        return redirect('dashboard')

    return render(request, 'career_app/admin_dashboard.html')


@login_required
def super_admin_dashboard_view(request):
    if not request.user.is_superuser:
        return redirect('dashboard')

    return render(request, 'career_app/super_admin_dashboard.html')