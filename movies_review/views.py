from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Moviess
from .serializer import MoviesSerializer

# Create your views here.

@api_view(['GET'])
def movies_list(request):
	if request.method == 'GET':
		obj = Moviess.objects.all()
		print ("________",obj)
		serializer = MoviesSerializer(obj,many=True)
		return Response(serializer.data)
