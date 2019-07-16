from django.conf.urls import url

from api.views import commands, cancel

urlpatterns = [
    url(r'^commands/$', commands),
    url(r'^cancel/$', cancel),
]
