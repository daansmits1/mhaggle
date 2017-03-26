from django.contrib import admin
from .models import Movie, Score, Toseelist

# class ActorAdmin(admin.ModelAdmin):
# 	list_display = ('name', )
# 	filter_horizontal = ('movies',)

class ToseelistAdmin(admin.ModelAdmin):
	list_display = ('user', )
	filter_horizontal = ('movies',)

admin.site.register(Movie)
admin.site.register(Toseelist, ToseelistAdmin)
admin.site.register(Score)
# admin.site.register(Actor, ActorAdmin)


