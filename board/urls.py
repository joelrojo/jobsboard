from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$', 'board.views.home', {}, 'home'),
    (r'^search$', 'board.views.search', {}, 'search'),
)