from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls_v2/', include('polls.urls')),
    url(r'^', include('main.urls')),
]
