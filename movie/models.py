from django.db import models

class Protagonist(models.Model):
	name = models.CharField(max_length=30, blank=True)
	
	
	def __str__(self):
		return self.name
	
class Movie(models.Model):
	name = models.CharField(max_length=30)
	main_leader = models.ManyToManyField(Protagonist)
	comment = models.TextField(blank=True)
	favorite = models.BooleanField(default=False)
