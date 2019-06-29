from django.conf.urls import url

from api.views import ready

urlpatterns = [
    url(r'^ready/$', ready),
]
