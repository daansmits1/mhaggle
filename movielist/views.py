from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from movielist.models import Movie
from django.contrib.auth.decorators import login_required


def home(request):
	full_list = Movie.objects.all()
	return render(request, 'movielist/intro.html', {"full_list": full_list})

def intro(request):
	full_list = Movie.objects.all()
	return render(request, 'movielist/intro.html', {"full_list": full_list})

def detail(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	return render(request, 'movielist/detail.html', {'movie': movie})

def search(request):
	search = request.GET.get("search_terms")
	if search:
		search_list = Movie.objects.filter(title__icontains=search)
		return render(request, 'movielist/search.html', {"search_list": search_list})
	return render(request, 'movielist/search.html')

@login_required
def movielist_personal(request):
	return render(request, 'movielist/movielist_personal.html')