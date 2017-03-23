from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from decimal import *

# Create your models here.

class Movie(models.Model):
	title_year = models.CharField(max_length=100)
	title = models.CharField(max_length=100)
	year = models.IntegerField()
	# description = models.TextField(max_length=5000, blank=True, default="") #don't need both
	# language = models.CharField(max_length=50)
	# picture_link = FileField()
	genre = models.CharField(max_length=200)
	# stars = models.CharField(max_length=100)
	length_min = models.IntegerField()
	rating_overall = models.DecimalField(max_digits=2, decimal_places=1)
	# actor = models.ManyToManyField(Actor, blank=True) 	
	votes = models.IntegerField(default=0)
	# wishlist_users = model.ManyToManyField(User, through='Wishlist') #wishees? ratees?
	def __str__(self):
		return self.title_year

class Rating(models.Model):
	movie = models.ForeignKey(Movie)
	pub_date = models.DateTimeField('date published')
	user_name = models.CharField(max_length=100) 
	rating = models.DecimalField(max_digits=3, decimal_places=1, null=True) #rating-->value

	def __str__(self):
		return self.user_name #user.name

class Wishlist(models.Model):
	movie = models.ForeignKey(Movie) 
	pub_date = models.DateTimeField('date published')
	user_name = models.CharField(max_length=100)
	#add user as other ForeignKey? --> allows for easier lookup of wishlist for user (user.wishlist.all()). Same for Ratings. After ManyToMany for Movie!
	# on_delete 
	wishlist = models.BooleanField()

	def __str__(self):
		return self.user_name

class Actor(models.Model):
	name = models.CharField(max_length=30)
	movies = models.ManyToManyField(Movie) 
	user_name = models.CharField(max_length=100)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.name

class Seenlist(models.Model):
	movies = models.ManyToManyField(Movie) 
	pub_date = models.DateTimeField('date published')
	user = models.OneToOneField(User)
	#add user as other ForeignKey? --> allows for easier lookup of wishlist for user (user.wishlist.all()). Same for Ratings. After ManyToMany for Movie!
	# on_delete 
	seenlist = models.BooleanField()

	def __str__(self):
		return self.user.username







