from django.forms import ModelForm, Form
from movielist.models import Rating, Toseelist

class RatingForm(ModelForm):
	class Meta:
		model = Rating
		fields = ['rating']
		widgets = {}

class ToseelistForm(ModelForm):
	class Meta:
		model = Toseelist
		fields = ['toseelist']
		widgets = {}

# class ActorForm(ModelForm):
# 	class Meta:
# 		model = Actor
# 		fields = ['name']
# 		widgets = {}

