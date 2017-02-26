__author__ = 'ASHISH'
from django import forms
from django.contrib.auth.admin import User
from .models import Album, Song, Profile


class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class Registration(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]


class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = [
            'album_title',
            'artist',
            'genre',
            'album_logo'
        ]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'name',
            'profile_picture',
            'bio'
        ]


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = [
            'track',
            'track_file'
        ]