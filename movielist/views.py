from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from movielist.models import Movie, Rating, Toseelist
from movielist.forms import RatingForm, ToseelistForm
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
	form_r = RatingForm(request.POST or None)
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
	form_t = ToseelistForm(request.POST or None)
	if form_t.is_valid():
		tosee = form_t.cleaned_data['toseelist']
		user = request.user
		if user.toseelist:
			toseelist = user.toseelist
		else:
			toseelist = user.toseelist.create()
		# toseelist = user.toseelist.get_or_create(user=user)
		# try if get or create works (instead of create, delete all else)
		toseelist.pub_date = datetime.datetime.now()
		toseelist.seenlist = tosee
		toseelist.save()
		toseelist.movies.add(movie)
	messages.success(request, "Successfully saved")
		# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie,)) Don't get this to work
	return render(request, 'movielist/detail.html', {'movie': movie, 'form_t': form_t} )

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
