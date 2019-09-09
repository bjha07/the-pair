#from django.conf.urls.defaults import *
#from django.conf.urls import patterns , url
from django.conf.urls import patterns, url
#from django.contrib.auth import views as auth_views
#from authentication import views as auviews


urlpatterns = patterns('authentication.views',
                      url(r'^$','login_authenticate'),
                      )

