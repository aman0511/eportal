from django.conf.urls import patterns, include, url
import notifications
from django.conf.urls import *

urlpatterns = patterns('notification.views',
    # Examples:
    url('^inbox/notifications/', include(notifications.urls)),
    url(r'^all/$', 'all', name='all'),
    url(r'^unread/$', 'unread', name='unread'),
    url(r'^mark-all-as-read/$', 'mark_all_as_read', name='mark_all_as_read'),
    url(r'^mark-as-read/(?P<slug>\d+)/$', 'mark_as_read', name='mark_as_read'),
    url(r'^mark-as-unread/(?P<slug>\d+)/$', 'mark_as_unread', name='mark_as_unread'),
    url(r'^delete/(?P<slug>\d+)/$', 'delete', name='delete'),

)