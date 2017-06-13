from django.db import models


class SongFavorite(models.Manager):
    def get_song_count(self):
        return self.filter(favorite=True).count()


class Song(models.Model):
    name = models.CharField(max_length=50)
    singer = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='img', null=True)
    favorite = models.BooleanField(default=False)
    music  = models.FileField(upload_to='music', null=True)
    objects = SongFavorite()

    def __str__(self):
        return self.name
