from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import UserForm, UserModelForm

# Create your views here.

def index(request):
    return render(request, 'mainsite/index.html')

def register(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        # print(user.email) Check user email is saved
        login(request, user)
        return redirect(reverse('index'))
        # render means templates folder, reverse means urls folder

    return render(request, 'registration/register.html', {'form': form})

def edit(request):
    form = UserModelForm(request.POST or None, instance=request.user)

    if form.is_valid():
        form.save()
        return redirect('index')

    return render(request, 'registration/edit.html', {'form':form})