from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from movielist.models import Movie, Score, Toseelist
from movielist.forms import ScoreForm, ToseelistForm
from django.core.urlresolvers import reverse	
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
import datetime


def home(request):
	full_list = Movie.objects.all()
	return render(request, 'movielist/intro.html', {"full_list": full_list})

def intro(request):
	full_list = Movie.objects.all()
	return render(request, 'movielist/intro.html', {"full_list": full_list})

def detail(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	form_s = ScoreForm(request.POST or None)
	form_t = ToseelistForm(request.POST or None)
	user = request.user
	if form_s.is_valid():
	# Test if it already exists (combination movie and user id). If so, drop that one and then create the new one
		score = Score()
	# rating = user.rating_set.get_or_create(movie=movie)?
		score.movies = movie
		score.score = form_s.cleaned_data['score'] # make sure you don't overwrite if it has already been set
		score.user = user
		# if score.score != none --> update the score
		score.pub_date = datetime.datetime.now()
		score.save()
	if form_t.is_valid():
		if user.toseelist:
			toseelist = user.toseelist
		else:
			toseelist = user.toseelist.create()
		toseelist.pub_date = datetime.datetime.now()
		toseelist.save()
		toseelist.movies.add(movie)
	messages.success(request, "Successfully saved")
		# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie,)) Don't get this to work
	return render(request, 'movielist/detail.html', {'movie': movie, 'form_s': form_s, 'form_t': form_t} )

def search(request):
	search = request.GET.get("search_terms")
	if search:
		search_list = Movie.objects.filter(title__icontains=search)
		return render(request, 'movielist/search.html', {"search_list": search_list})
	return render(request, 'movielist/search.html')

@login_required
def wishlist(request):
	toseelist = request.user.toseelist
	movies = toseelist.movies.all
	return render(request, 'movielist/wishlist.html', {"movies": movies})

@login_required
def score_list(request):
	if request.user.is_authenticated(): # This is not necessary if you also have login_required. Change after deciding setup of page
		score_list = Score.objects.filter(user=request.user)
	else: 
		score_list = Score.objects.all()
	return render(request, 'movielist/score_list.html', {"score_list": score_list})


# @login_required
# do you want to make profile page public? otherwise maybe dashboard
def profile_page(request):
	username = request.POST["username"]
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		# Probably need to do: if user-authenticated, don't login again
		# if user.is_active:
		# 	login(request, user)
		return render(request, 'movielist/profile_page.html')
	else: 
		error = "Something went wrong, please try again"
		return render(request, 'registration/login.html', {"error": error})


def test(request):
	return render(request, "movielist/test.html")
