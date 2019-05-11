from rest_framework import serializers
from .models import Moviess

class MoviesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Moviess
		fields = ('id','popularity','director','imdb_score','name')