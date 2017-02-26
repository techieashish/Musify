from django.db import models
from django.contrib.auth.admin import User


class Album(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=100)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()


    def __str__(self):
        return self.album_title


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    track = models.CharField(max_length=100)
    track_file = models.FileField()

    def __str__(self):
        return self.track


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    profile_picture = models.FileField()
    bio = models.TextField()

    def __str__(self):
        return self.name
