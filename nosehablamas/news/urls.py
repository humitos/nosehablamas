from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('news.views',
    url(r'^$', 'home', name='news__home'),
    url(r'^news/add/$', 'add_news', name='news__add_news'),
    url(r'^article/add/$', 'add_article', name='news__add_article'),
)
