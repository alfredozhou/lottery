from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lottery.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
 	url(r'^time-to-buy/$', 'lotto_web.views.better_lotto_status'),
    url(r'^admin/', include(admin.site.urls)),
)
