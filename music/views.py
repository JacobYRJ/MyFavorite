from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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
        song.music = request.FILES['music']
        song.save()
        return render(request, 'music/detail.html', {'song': song})
    context = {
        'form': form,
    }
    return render(request, 'music/add_song.html', context)


@login_required
def favorite(request, song_id):
    song = get_object_or_404(Song, pk=song_id)
    try:
        if song.favorite:
            song.favorite = False
        else:
            song.favorite = True
        song.save()
    except(KeyError, Song.DoesNotExist):
        return JsonResponse({'success': False})
    else:
        return JsonResponse({'success': True})


@login_required
def delete_song(request, song_id):
    song = Song.objects.get(pk=song_id)
    song.delete()
    return render(request, 'music/detail.html', {'song': song})
