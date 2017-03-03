from django.conf.urls import include,url

from . import views

urlpatterns = [
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^$', views.intro, name='intro'),
    url(r'^search/$', views.search, name='search'),
    url(r'^personallist/$', views.movielist_personal, name='personal')
]