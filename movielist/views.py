from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
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
	if user.score_set.get(movies=movie):
		score = user.score_set.get(movies=movie)
	else:
		score = ("")
	return render(request, 'movielist/detail.html', {'score':score, 'movie': movie, 'form_s': form_s, 'form_t': form_t} )
	# return render(request, 'movielist/detail.html', {'movie': movie, 'form_s': form_s, 'form_t': form_t} )
	# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie, form_s, form_t))

def score_submission(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	form_s = ScoreForm(request.POST or None) 
	form_t = ToseelistForm(request.POST or None) #do we need this?
	user = request.user
	if form_s.is_valid():
		score = Score()
		score.movies = movie
		score.score = form_s.cleaned_data['score'] 
		score.user = user
		score.pub_date = datetime.datetime.now()
		score.save()
# 		# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie,)) Don't get this to work
	return redirect('movielist:detail', movie_id= movie.id)

def score_update(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	form_s = ScoreForm(request.POST or None) 
	form_t = ToseelistForm(request.POST or None) #do we need this?
	user = request.user
	score = user.score_set.get(movies=movie)
	if form_s.is_valid():
		score.delete()
		score = Score()
		score.movies = movie
		score.score = form_s.cleaned_data['score'] 
		score.user = user
		score.pub_date = datetime.datetime.now()
		score.save()
# 		# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie,)) Don't get this to work
	return redirect('movielist:detail', movie_id= movie.id)

def add_to_wishlist(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	form_s = ScoreForm(request.POST or None) #do we need this?
	form_t = ToseelistForm(request.POST or None)
	user = request.user
	if form_t.is_valid():
		if user.toseelist:
			toseelist = user.toseelist
		else:
			toseelist = user.toseelist.create()
		toseelist.pub_date = datetime.datetime.now()
		toseelist.save()
		toseelist.movies.add(movie)
	# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie, form_s, form_t))
	# return render(request, 'movielist/detail.html', {'movie': movie, 'form_s': form_s, 'form_t': form_t} )
	return redirect('movielist:detail', movie_id= movie.id)

def remove_from_wishlist(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	form_s = ScoreForm(request.POST or None)
	form_t = ToseelistForm(request.POST or None)
	user = request.user
	toseelist = user.toseelist
	if form_t.is_valid():
		toseelist.movies.remove(movie)
	return redirect('movielist:detail', movie_id= movie.id)


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


@login_required
# do you want to make profile page public? otherwise maybe dashboard
def profile_page(request):
	user = request.user
	return render(request, 'movielist/profile_page.html')

def login(request, error=None):
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
		return render(request, 'registration/login.html')

def test(request):
	return render(request, "movielist/test.html")
