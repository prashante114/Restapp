from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Moviess
from .serializer import MoviesSerializer,UserSerilazer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from rest_framework.views import APIView

# Create your views here.

# @api_view(['GET'])
# def movies_list(request):
# 	if request.method == 'GET':
# 		obj = Moviess.objects.all()
# 		serializer = MoviesSerializer(obj,many=True)
# 		return Response(serializer.data)

class MovieeView(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request):
		query_set = Moviess.objects.all()
		serializer = MoviesSerializer(query_set,many=True)
		return Response(serializer.data)

class CreateMovieeView(CreateAPIView):
	permission_classes = (IsAuthenticated,IsAdminUser)
	query_set = Moviess.objects.all()
	serializer_class = MoviesSerializer

class CreateUserView(CreateAPIView):
	model = get_user_model()
	serializer_class = UserSerilazer
	


