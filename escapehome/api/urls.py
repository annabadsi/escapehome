from django.conf.urls import url

from api.views import ready, commands

urlpatterns = [
    url(r'^ready/$', ready),
    url(r'^commands/$', commands),
]
