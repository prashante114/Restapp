from rest_framework import serializers
from .models import Moviess
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated

class MoviesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Moviess
		fields = ('id','popularity','director','imdb_score','name')

class UserSerilazer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)

	def create(self,validated_data):
		user = get_user_model().objects.create(
			username = validated_data['username'])
		user.set_password(validated_data['password'])
		user.save()
		return user
	class Meta:
		model = get_user_model()
		fields = ('username','password')
