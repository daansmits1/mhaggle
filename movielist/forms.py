from django.forms import ModelForm
from movielist.models import Wishlist, Rating

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
	# rating = maybe set up as form not as ModelForm (watch the import!) 

