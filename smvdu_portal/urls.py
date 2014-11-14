from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    (r'^quizes/',include('quiz.urls')),
    url(r'^$', 'student.views.home', name='home'),
    url(r'^login$', 'student.views.login_view', name='login'),
    url(r'^course$', 'student.views.courseView', name='courses'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^faculty$', 'student.views.faculty', name='faculty'),
    url(r'^about$', 'smvdu_portal.views.about', name='about'),
    url(r'^logout$', 'student.views.logout_view', name='logout'),
    url(r'^reset/$', 'student.views.reset', name='reset'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'student.views.reset_confirm', name='password_reset_confirm'),
    url(r'^success/$', 'student.views.success', name='success'),
    url(r'^edit/$', 'student.views.edit', name='edit'),
    
)