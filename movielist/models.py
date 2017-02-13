from django.db import models
from django.utils import timezone
from decimal import Decimal

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
	rating_overall = models.DecimalField(max_digits=5, decimal_places=3)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.title_year


# class Movielist_personal:
# ForeignKey!!
# 	user_id = models.CharField(max_length=30)
# 	seen = models.BooleanField()
# 	rating_personal_voted = models.Decimalfield(max_digits=5, decimal_places=3)
# 	rating_personal_calc = models.Decimalfield(max_digits=5, decimal_places=3)
# 	date_voted = model.DateTimeField()

