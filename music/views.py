from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import SongForm
from .models import Song

IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']


@login_required
def index(request):

    return render(request, 'music/index.html')


@login_required
def detail(request):
    song = Song.objects.order_by('name')
    context = {
        'song': song
    }
    return render(request, 'music/detail.html', context)


@login_required
def add_song(request):
    form = SongForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        song = form.save(commit=False)
        song.cover = request.FILES['cover']

        song.save()
        return render(request, 'music/detail.html', {'song': song})
    context = {
        'form': form,
    }
    return render(request, 'music/add_song.html', context)
