from django.conf.urls import patterns, include, url
from .views import AuthView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', AuthView.as_view(), name='auth'),
    # url(r'^/', include('.foo.urls')),

)