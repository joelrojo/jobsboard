from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^/private/admin/', include(admin.site.urls)),
    url(r'^', include('board.urls')),
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/img/favicon.ico'}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': 'board/static'}),
)