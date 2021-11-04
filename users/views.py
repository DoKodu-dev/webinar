from .models import Entry
from datetime import datetime
from django.http import JsonResponse
from django.shortcuts import render
from .forms import MySignupForm, EntryForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def save_vote(request):
    entry_id = request.POST['entry_id']
    entry = Entry.objects.get(pk=entry_id)
    entry.votes.up(request.user.id)
    entry = Entry.objects.get(pk=entry_id)

    return JsonResponse({
        'entry_id': entry_id,
        'vote_score': entry.vote_score
    })


def main(request):
    entries = Entry.objects.all()
    return render(
        request,
        'home.html',
        context={
            'entries': entries
        }
    )


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
    if request.method == 'POST':
        form = EntryForm(request.POST, request.FILES)
        entry = form.save(commit=False)
        entry.author = request.user
        entry.pub_date = datetime.now()
        entry.save()

    form = EntryForm()
    entries = Entry.objects.order_by('-pub_date')

    return render(
        request,
        'users/panel.html',
        {
            'form': form,
            'entries': entries
        }

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
