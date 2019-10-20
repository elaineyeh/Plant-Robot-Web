from django.shortcuts import render

from .models import Post
from .forms import TodoModelForm, DeleteConfirmForm
from .filters import PostFilter
from django.shortcuts import redirect, get_object_or_404

from django.contrib.auth.decorators import login_required


def index(request):
    _filter = PostFilter(
        request.GET or None,
        queryset=Post.objects.all()
    )
    return render(
        request, 'todo/index.html', {
            'todos': _filter.qs.all(),
            'filter': _filter
        }
    )


@login_required
def new(request):
    form = TodoModelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        todo = form.save(request.user)  # Save without database
        todo.creator = request.user
        form.save(user=request.user)
        return redirect('todo:index')

    return render(request, 'todo/new.html', {
        'form': form
    })


@login_required
def delete(request, pk):
    form = DeleteConfirmForm(request.POST or None)

    if form.is_valid() and form.cleaned_data['check']:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('todo:index')

    return render(request, 'todo/delete.html', {
        'form': form
    })


@login_required
def edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = TodoModelForm(
        request.POST or None,
        request.FILES or None,
        instance=post
    )

    if form.is_valid():
        post.creator = request.user
        form.save(request.user)
        return redirect('todo:index')

    return render(request, 'todo/edit.html', {
        'form': form
    })


def show(request, pk):
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'todo/show.html', {
        'post':post
    })
