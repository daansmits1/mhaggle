from django.forms import ModelForm, Form
from movielist.models import Score, Toseelist

class ScoreForm(ModelForm):
	class Meta:
		model = Score
		fields = ['score']
		widgets = {}

class ToseelistForm(Form):
	class Meta:
		model = Toseelist
		widgets = {}

# class ActorForm(ModelForm):
# 	class Meta:
# 		model = Actor
# 		fields = ['name']
# 		widgets = {}

