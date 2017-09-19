from django.conf.urls import url

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login_user, name='login'),
    url(r'^logout$', views.logout_user, name='logout'),
    url(r'^word$', views.word, name='word'),
    url(r'^word/(?P<id>[0-9]+)/$', views.word_individual, name="word_individual"),
    url(r'^word/(?P<id>[0-9]+)/delete$', views.word_delete, name="word_delete"),
    url(r'^word/(?P<id>[0-9]+)/update$', views.word_update, name="word_update"),
    url(r'^home$', views.home, name='home'),
    url(r'^my-words$', views.my_words, name='mywords'),
]
