from django.conf.urls import include,url

from . import views

urlpatterns = [
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.intro, name='intro'),
    url(r'^search/$', views.search, name='search'),
    url(r'^wishlist/$', views.wishlist, name='wishlist'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile_page/$', views.profile_page, name='profile_page'),
	url(r'^score_list/$', views.score_list, name='score_list'),
	url(r'^add_to_wishlist/(?P<movie_id>[0-9]+)/$', views.add_to_wishlist, name="add_to_wishlist"),
	url(r'^remove_from_wishlist/(?P<movie_id>[0-9]+)/$', views.remove_from_wishlist, name="remove_from_wishlist"),
	url(r'^score_submission/(?P<movie_id>[0-9]+)/$', views.score_submission, name="score_submission"),
	url(r'^score_update/(?P<movie_id>[0-9]+)/$', views.score_update, name="score_update"),
	url(r'^test/$', views.test, name='test')
]