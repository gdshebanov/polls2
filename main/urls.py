from django.conf.urls import url
from . import views

app_name = 'main'
urlpatterns = [
    url(r'^$', views.start_page, name='start_page'),
    url(r'^check/$', views.check, name='check'),
]
