from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from movielist.models import Movie, Wishlist, Rating
from movielist.forms import WishlistForm, RatingForm
from django.core.urlresolvers import reverse	
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
import datetime


def home(request):
	full_list = Movie.objects.all()
	return render(request, 'movielist/intro.html', {"full_list": full_list})

def intro(request):
	full_list = Movie.objects.all()
	return render(request, 'movielist/intro.html', {"full_list": full_list})

def detail(request, movie_id):
	movie = get_object_or_404(Movie, pk=movie_id)
	form_w = WishlistForm(request.POST)
	form_r = RatingForm(request.POST)
	full_list = Movie.objects.all()
	if form_w.is_valid():
		wishes = form_w.cleaned_data['wishlist']
		user_name = request.user.username
		wishlist = Wishlist()
		wishlist.movie = movie
		wishlist.wishlist = wishes
		wishlist.user_name = user_name
		wishlist.pub_date = datetime.datetime.now()
		wishlist.save()
	if form_r.is_valid():
		rate = form_r.cleaned_data['rating']
		user_name = request.user.username
		rating = Rating()
		rating.movie = movie
		rating.rating = rate
		rating.user_name = user_name
		rating.pub_date = datetime.datetime.now()
		rating.save()
		# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie,)) Don't get this to work
		return render(request, 'movielist/intro.html', {"full_list": full_list})		
	return render(request, 'movielist/detail.html', {'movie': movie, 'form_w': form_w, 'form_r': form_r})

# def detail(request, movie_id):
# 	movie = get_object_or_404(Movie, pk=movie_id)
# 	form = WishlistForm(request.POST)
# 	full_list = Movie.objects.all()
# 	if form.is_valid():
# 		wishes = form.cleaned_data['wishlist']
# 		user_name = request.user.username
# 		wishlist = Wishlist()
# 		wishlist.movie = movie
# 		wishlist.wishlist = wishes
# 		wishlist.user_name = user_name
# 		wishlist.pub_date = datetime.datetime.now()
# 		wishlist.save()
# 		# return HttpResponseRedirect(reverse('movielist:detail'), args=(movie,)) Don't get this to work
# 		return render(request, 'movielist/intro.html', {"full_list": full_list})		
# 	return render(request, 'movielist/detail.html', {'movie': movie, 'form': form})

def search(request):
	search = request.GET.get("search_terms")
	if search:
		search_list = Movie.objects.filter(title__icontains=search)
		return render(request, 'movielist/search.html', {"search_list": search_list})
	return render(request, 'movielist/search.html')

@login_required
def wishlist(request):
	if request.user.is_authenticated():
		full_list = Wishlist.objects.filter(wishlist=1, user_name=request.user)
	else: 
		full_list = Wishlist.objects.filter(wishlist=1)
	return render(request, 'movielist/wishlist.html', {"full_list": full_list})


# @login_required
# do you want to make profile page public? otherwise maybe dashboard
def profile_page(request):
	username = request.POST["username"]
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		login(request, user)
		# if user.is_active:
		# 	login(request, user)
		full_list = Wishlist.objects.filter(wishlist=1)
		return render(request, 'movielist/profile_page.html', {"full_list": full_list, "username": username})
	else: 
		error = "Something went wrong, please try again"
		return render(request, 'registration/login.html', {"error": error})
