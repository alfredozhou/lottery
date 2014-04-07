from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'lotto_web.views.index', name='home'),
    url(r'^year-view$', 'lotto_web.views.yearView', name='year-view'),
    url(r'^start-registering$', 'lotto_web.registration.start_registering', name='start-registering'),
    url(r'^register$', 'lotto_web.registration.register', name='register'),
    url(r'^sign-in$', 'lotto_web.registration.sign_in', name='sign-in'),
    url(r'^sign-out$', 'lotto_web.registration.sign_out', name='sign-out'),
    url(r'^start-uploading$', 'lotto_web.ticketupload.show', name='start-uploading'),
    url(r'^upload-pic$', 'lotto_web.ticketupload.upload', name='upload-pic'),
    url(r'^edit_ticket$', 'lotto_web.ticketupload.edit_ticket', name='edit_ticket'),
    url(r'^lotto-purchases$', 'lotto_web.numberOfTickets.lottosPurchased'),
    url(r'^svg-view$', 'lotto_web.views.svgView'),
 	url(r'^time-to-buy/$', 'lotto_web.views.better_lotto_status', name='time-to-buy'),
    url(r'^admin/', include(admin.site.urls)),
)
