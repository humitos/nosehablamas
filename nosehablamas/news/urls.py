from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('news.views',
    url(r'^$', 'home', name='home'),
)
