from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.polls, name='list'),
    url(r'^(?P<poll_id>[0-9]+)/$', views.poll_detail, name='detail'),
    url(r'^(?P<poll_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
