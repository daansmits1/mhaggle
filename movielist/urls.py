from django.conf.urls import include,url

from . import views

urlpatterns = [
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.intro, name='intro'),
    url(r'^search/$', views.search, name='search'),
    url(r'^wishlist/$', views.wishlist, name='wishlist'),
    url(r'^profile_page/$', views.profile_page, name='profile_page'),
	url(r'^rating_list/$', views.rating_list, name='rating_list'),
]