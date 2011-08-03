from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from tck.iller.views import *

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', iller),
    url(r'^yolnotlari^', 'yolnotlar'),
    url(r'^yolnotlari/(.*)', 'yolnotlar'),
    url(r'^yolnotlari/(.*)/(.*)', 'yolnotlar'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^iller/','iller.views.iller'),
)
