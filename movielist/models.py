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
	# raters = models.ManyToManyField(User, through='Score')
	def __str__(self):
		return self.title_year

# can we change this to a manytomany relationship? The difference with the Toseelist is that you have to add the rating to each relationship
class Rating(models.Model):
	movies = models.ForeignKey(Movie) 
	pub_date = models.DateTimeField('date published')
	user = models.ForeignKey(User) 
	rating = models.DecimalField(max_digits=3, decimal_places=1, null=True) #rating-->value

	def __str__(self):
		return self.user.username

# can we change this to a manytomany relationship? The difference with the Toseelist is that you have to add the rating to each relationship
class Score(models.Model):
	movies = models.ForeignKey(Movie) 
	pub_date = models.DateTimeField('date published')
	user = models.ForeignKey(User) 
	score = models.DecimalField(max_digits=3, decimal_places=1, null=True)	 #rating-->value

	def __str__(self):
		return self.user.username


# class Actor(models.Model):
# 	name = models.CharField(max_length=30)
# 	movies = models.ManyToManyField(Movie) 
# 	user_name = models.CharField(max_length=100)
# 	pub_date = models.DateTimeField('date published')

# 	def __str__(self):
# 		return self.name

class Toseelist(models.Model):
	movies = models.ManyToManyField(Movie) 
	pub_date = models.DateTimeField('date published')
	user = models.OneToOneField(User)
	# on_delete 

	def __str__(self):
		return self.user.username







