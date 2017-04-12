from django.db import models
from django.contrib.auth.models import  User


class Muzikland(models.Model):
	user = models.ForeignKey(User, default=1)
	artist = models.CharField(max_length=250)
	muzikland_title = models.CharField(max_length=500)
	muzikland_style = models.CharField(max_length=100)
	muzikland_logo = models.FileField()
	is_favorite = models.BooleanField(default=False)
	
	def __str__(self):
		return self.muzikland_title
	

class Song(models.Model):
	muzikland = models.ForeignKey(Muzikland, on_delete=models.CASCADE)
	song_name = models.CharField(max_length=250)
	audio_file = models.FileField(default='')
	is_favorite = models.BooleanField(default=False)
	
	def __str__(self):
		return self.song_name