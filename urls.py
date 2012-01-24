from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mpthree.views.home', name='home'),
    # url(r'^mpthree/', include('mpthree.foo.urls')),
    url(r'^$', 'player.views.index', name='index'),
    url(r'^playlist/(\d+)?', 'player.views.load_playlist'),
    url(r'^file/(\d+)?', 'player.views.serve_mp3'),
    url(r'^filebrowser$', 'player.views.filebrowser_load'),
    url(r'^filebrowser_json$', 'player.views.filebrowser_load_json'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
