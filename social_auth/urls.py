"""URLs module"""
from django.conf.urls.defaults import patterns, url

from social_auth.views import auth, register, complete, associate, associate_complete, \
                              disconnect


urlpatterns = patterns('',
    url(r'^register/(?P<backend>[^/]+)/$', register, name='socialauth_register_begin'),
    url(r'^register/complete/(?P<backend>[^/]+)/$', complete, kwargs={'create_user': True}, name='socialauth_register_complete'),
    url(r'^login/(?P<backend>[^/]+)/$', auth, name='socialauth_begin'),
    url(r'^complete/(?P<backend>[^/]+)/$', complete, kwargs={'create_user': False}, name='socialauth_complete'),
    url(r'^associate/(?P<backend>[^/]+)/$', associate, name='socialauth_associate_begin'),
    url(r'^associate/complete/(?P<backend>[^/]+)/$', associate_complete,
        name='socialauth_associate_complete'),
    url(r'^disconnect/(?P<backend>[^/]+)/$', disconnect, name='socialauth_disconnect'),
    url(r'^disconnect/(?P<backend>[^/]+)/(?P<association_id>[^/]+)/$', disconnect,
        name='socialauth_disconnect_individual'),
)
