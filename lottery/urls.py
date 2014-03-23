from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'lotto_web.views.index', name='home'),
    url(r'^year-view$', 'lotto_web.views.yearView', name='year-view'),
    url(r'^lotto-purchases$', 'lotto_web.numberOfTickets.lottosPurchased'),
    url(r'^svg-view$', 'lotto_web.views.svgView'),
 	url(r'^time-to-buy/$', 'lotto_web.views.better_lotto_status'),
    url(r'^admin/', include(admin.site.urls)),
)
