from django.conf.urls import url
from . import views
app_name = 'tweetlist'


urlpatterns = [
    url(r'^$', views.home , name='home'),
    url(r'^listweets$', views.listweets, name='listweets'),
]
