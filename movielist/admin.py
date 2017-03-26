from django.contrib import admin
from .models import Movie, Rating, Toseelist

# class ActorAdmin(admin.ModelAdmin):
# 	list_display = ('name', )
# 	filter_horizontal = ('movies',)

# class SeenlistAdmin(admin.ModelAdmin):
# 	list_display = ('movie', )
# 	filter_horizontal = ('users',)

admin.site.register(Movie)
admin.site.register(Toseelist)
admin.site.register(Rating)
# admin.site.register(Actor, ActorAdmin)


