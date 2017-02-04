from django.http import HttpResponse
from django.shortcuts import render
from movielist.models import Movie

def intro(request):

	full_list = Movie.objects.all()
	return render(request, 'movielist/intro.html', {"full_list": full_list})