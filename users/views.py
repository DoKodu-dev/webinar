from django.shortcuts import render
from .forms import MySignupForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = MySignupForm(request.POST)
        if form.is_valid():
            user = form.save()

    form = MySignupForm()
    return render(
        request,
        'users/register.html',
        context={
            'form': form
        }
    )


@login_required
def panel(request):
    return render(
        request,
        'users/panel.html'
    )


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)

    form = AuthenticationForm()

    return render(
        request,
        'users/login.html',
        context={
            'form': form
        }
    )
