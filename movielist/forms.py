from django.forms import ModelForm
from movielist.models import Wishlist, Rating, Actor, Seenlist

class RatingForm(ModelForm):
	class Meta:
		model = Rating
		fields = ['rating']
		widgets = {}

class WishlistForm(ModelForm):
	class Meta:
		model = Wishlist
		fields = ['wishlist']
		widgets = {}

class SeenlistForm(ModelForm):
	class Meta:
		model = Seenlist
		fields = ['seenlist']
		widgets = {}

class ActorForm(ModelForm):
	class Meta:
		model = Actor
		fields = ['name']
		widgets = {}

