from django.db import models

# Create your models here.
class Moviess(models.Model):
	popularity= models.CharField(max_length=30, blank=True)
	director = models.CharField(max_length=30, blank=True)
	imdb_score = models.DecimalField(max_digits=10,decimal_places=2)
	name = models.CharField(max_length=30)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name

	