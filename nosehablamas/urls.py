from django.conf import settings
from django.conf.urls.defaults import patterns, include, url
from django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nosehablamas.views.home', name='home'),
    # url(r'^nosehablamas/', include('nosehablamas.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'', include('news.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# We need this two-next lines because we are not using the default
# "runserver" command
# https://docs.djangoproject.com/en/dev/howto/static-files/#serving-static-files-in-development
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()
