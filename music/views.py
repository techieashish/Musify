from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import Login, Registration, AlbumForm, ProfileForm, SongForm
from .models import Song, Album, Profile


def index(request):
    if request.user.is_authenticated():
        return redirect('music:albums')
    return redirect('music:login')


def user_login(request):
    form = Login(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            return redirect('music:dash')

    return render(request, 'music/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('music:login')


def user_registration(request):
    form = Registration(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        email = form.cleaned_data['email']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('music:create')
    return render(request, 'music/register.html', {'form': form})


def dash(request):
    profile = Profile.objects.filter(user=request.user)
    return render(request, 'music/dash.html', {'profile': profile})


def albums(request):
    if not request.user.is_authenticated():
        return redirect('music:login')
    else:
        user_albums = request.user.album_set.all()
        return render(request, 'music/albums.html', {'albums': user_albums})


def create_profile(request):
    if not request.user.is_authenticated():
        redirect('music:login')
    else:
        form = ProfileForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('music:dash')
        return render(request, 'music/profile.html', {'form': form})


def album(request, album_id):
    album_detail = get_object_or_404(Album, pk=album_id)
    print(album_id)
    return render(request, 'music/album.html', {'album': album_detail})


def add_album(request):
    form = AlbumForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        new_album = form.save(commit=False)
        new_album.user = request.user
        new_album.save()
        return redirect('music:albums')
    return render(request, 'music/addAlbum.html', {'form': form})


def edit_album(request, album_id):
    album_detail = get_object_or_404(Album, pk=album_id)
    form = AlbumForm(request.POST or request.FILES or None, instance=album_detail)
    if form.is_valid():
        edited_album = form.save(commit=False)
        edited_album.user = request.user
        edited_album.save()
        return redirect('music:album', album_id=album_id)
    return render(request, 'music/albumedit.html', {'form': form, 'album': album_detail})


def album_delete(request, album_id):
    selected_album = get_object_or_404(Album, pk=album_id)
    selected_album.delete()
    return redirect('music:albums')


def add_song(request, album_id):
    form = SongForm(request.POST or None,  request.FILES or None)
    if form.is_valid():
            new_song = form.save(commit=False)
            associated_album = get_object_or_404(Album, pk=album_id)
            new_song.album = associated_album
            new_song.save()
            return redirect('music:album', album_id= album_id)
    else:
        return render(request, 'music/addsong.html', {'form': form})


def songs(request):
    if not request.user.is_authenticated():
        return redirect('music:login')
    else:
        song_album = Album.objects.get(user=request.user)
        songs = song_album.song_set.all()
        return render(request, 'music/songs.html', {'songs': songs})


def song_delete(request, album_id, song_id):
    song_album = get_object_or_404(Album, pk=album_id)
    track = Song.objects.get(pk=song_id)
    track.delete()
    return redirect('music:album', album_id=album_id)


def edit_song(request, album_id, song_id):
    song_detail = get_object_or_404(Song, pk=song_id)
    form = SongForm(request.POST or request.FILES or None, instance=song_detail)
    associated_album = get_object_or_404(Album, pk=album_id)
    if form.is_valid():
        edited_song = form.save(commit=False)
        edited_song.album = associated_album
        edited_song.save()
        return redirect('music:album', album_id=album_id)
    return render(request, 'music/songedit.html', {'form': form, 'detail': song_detail})


def edit_profile(request):

    profile_details = Profile.objects.get(user=request.user)
    form = ProfileForm(request.POST or None, request.FILES or None, instance=profile_details)
    if request.POST:
        if form.is_valid():
            update = form.save(commit=False)
            update.user = request.user
            update.save()
            return redirect('music:dash')
    return render(request, 'music/editprofile.html', {'form': form, 'detail': profile_details})










