from django.conf.urls import url

from sport import views

urlpatterns = [
    url(r'$', views.index, name='index'),
    url(r'^register/$', views.register, name='resigster'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^playground/$', views.playground, name='playground'),
    url(r'^logout/$', views.user_logout, name='logouts')
]
