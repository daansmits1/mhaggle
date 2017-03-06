from django.forms import ModelForm
from movielist.models import Wishlist

# class RatingForm(ModelForm):
# 	class Meta:
# 		model = Rating
# 		fields = ['user_name','rating']
# 		widgets = {}


class WishlistForm(ModelForm):
	class Meta:
		model = Wishlist
		fields = ['wishlist', 'user_name']
		widgets = {}


