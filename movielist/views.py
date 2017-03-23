from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from movielist.models import Movie, Wishlist, Rating, Actor, Seenlist
from movielist.forms import WishlistForm, RatingForm, ActorForm, SeenlistForm
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
	# form_w = WishlistForm(request.POST or None)
	# form_r = RatingForm(request.POST or None)
	# form_a = ActorForm(request.POST or None)
	# actor_list = movie.actor_set.all()
	# if form_w.is_valid():
	# 	wishes = form_w.cleaned_data['wishlist']
	# 	user_name = request.user.username
	# 	wishlist = Wishlist()
	# 	wishlist.movie = movie
	# 	wishlist.wishlist = wishes
	# 	wishlist.user_name = user_name
	# 	wishlist.pub_date = datetime.datetime.now()
	# 	wishlist.save()
	# 	# many to may without creating new object
	# if form_r.is_valid():
	# 	rate = form_r.cleaned_data['rating']
	# 	user_name = request.user.username
	# 	rating = Rating()
	## rating = user.rating_set.get_or_create(movie=movie)?
	# 	rating.movie = movie
	# 	rating.rating = rate # make sure you don't overwrite if it has already been set
	# 	rating.user_name = user_name
	# 	rating.pub_date = datetime.datetime.now()
	# 	rating.save()
	# if form_a.is_valid():
	# 	name = form_a.cleaned_data['name']
	# 	user_name = request.user.username
	# 	actor = Actor()
	# 	# getorcreate! so it doesn't duplicate things
	# 	actor.name = name
	# 	actor.pub_date = datetime.datetime.now()
	# 	actor.save()
	# 	movie.actor_set.add(actor)
	form_s = SeenlistForm(request.POST or None)
	if form_s.is_valid():
		seen = form_s.cleaned_data['seenlist']
		user = request.user
		if user.seenlist:
			seenlist = user.seenlist
		else:
			seenlist = user.seenlist.create()
		# try if get or create works (instead of create, delete all else)
		seenlist.pub_date = datetime.datetime.now()
		seenlist.seenlist = seen
		seenlist.save()
		# movie.seenlist_set.add(seenlist)
		seenlist.movies.add(movie)
	messages.success(request, "Successfully saved")
		# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie,)) Don't get this to work
	# return render(request, 'movielist/detail.html', {'movie': movie, 'form_w': form_w, 'form_r': form_r, 'form_a': form_a, 'actor_list':actor_list} )
	return render(request, 'movielist/detail.html', {'movie': movie, 'form_s': form_s} )

# delete again after fixing many to many for rating and wishlist
def seenlist(request):
	# seen_list = Movie.objects.filter(seenlist__seen=True)
	seenlist = request.user.seenlist
	movies = seenlist.movies.all
	return render(request, 'movielist/seenlist.html', {'seenlist': seenlist, 'movies': movies} )

def actor(request):
	actor_list = Actor.objects.all()
	return render(request, 'movielist/actor.html', {'actor_list':actor_list} )

def search(request):
	search = request.GET.get("search_terms")
	if search:
		search_list = Movie.objects.filter(title__icontains=search)
		return render(request, 'movielist/search.html', {"search_list": search_list})
	return render(request, 'movielist/search.html')

@login_required
def wishlist(request):
	if request.user.is_authenticated(): # This is not necessary if you also have login_required. Change after deciding setup of page
		full_list = Wishlist.objects.filter(wishlist=True, user_name=request.user)
	else: 
		full_list = Wishlist.objects.filter(wishlist=True)
	return render(request, 'movielist/wishlist.html', {"full_list": full_list})

# @login_required
def rating_list(request):
	if request.user.is_authenticated(): # This is not necessary if you also have login_required. Change after deciding setup of page
		full_list = Rating.objects.filter(user_name=request.user)
	else: 
		full_list = Rating.objects.all()
	return render(request, 'movielist/rating_list.html', {"full_list": full_list})


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
		full_list = Wishlist.objects.filter(wishlist=True)
		return render(request, 'movielist/profile_page.html', {"full_list": full_list, "username": username})
	else: 
		error = "Something went wrong, please try again"
		return render(request, 'registration/login.html', {"error": error})
