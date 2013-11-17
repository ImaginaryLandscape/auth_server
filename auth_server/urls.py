from django.conf.urls import patterns, include, url
from .views import AuthView

urlpatterns = patterns('',
    url(r'^$', AuthView.as_view(), name='auth'),
)

