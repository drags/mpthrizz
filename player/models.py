from django.db import models

# Create your models here.

class MusicFile(models.Model):
        header = models.CharField(max_length=4)
        title = models.CharField(max_length=60)
        artist = models.CharField(max_length=60)
        album = models.CharField(max_length=60)
        speed = models.SmallIntegerField()
        genre = models.CharField(max_length=30)
        starttime = models.CharField(max_length=6)
        endtime = models.CharField(max_length=6)
        tracknumber = models.SmallIntegerField()
        path = models.CharField(max_length=2048)
        date_added = models.DateField(auto_now_add=True)

class Playlist(models.Model):
        name = models.CharField(max_length=60)
        created_on = models.DateField(auto_now_add=True)

class PlaylistEntry(models.Model):
        playlist = models.ForeignKey('Playlist')
        musicfile = models.ForeignKey('MusicFile')

class Rating(models.Model):
        file = models.ForeignKey('MusicFile')
        rating = models.SmallIntegerField()

