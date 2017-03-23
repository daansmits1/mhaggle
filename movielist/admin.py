from django.contrib import admin
from .models import Movie, Wishlist, Rating, Actor, Seenlist

class ActorAdmin(admin.ModelAdmin):
	list_display = ('name', )
	filter_horizontal = ('movies',)

# class SeenlistAdmin(admin.ModelAdmin):
# 	list_display = ('movie', )
# 	filter_horizontal = ('users',)

admin.site.register(Movie)
admin.site.register(Seenlist)
admin.site.register(Wishlist)
admin.site.register(Rating)
admin.site.register(Actor, ActorAdmin)


