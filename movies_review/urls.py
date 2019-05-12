


from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework.authtoken import views as rest_framework_views

urlpatterns = [
	path('',views.MovieeView.as_view()),
	path('movies_list/',views.MovieeView.as_view()),
    path('create_movies/',views.CreateMovieeView.as_view()),
    path('register/',views.CreateUserView.as_view(),name='user'),
]
