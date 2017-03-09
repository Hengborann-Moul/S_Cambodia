from django.conf.urls import url

from sport_user import views

urlpatterns = [
    url(r'^index/', views.index, name='index'),
    url(r'^register/$', views.register, name='resigster'),
    url(r'^$', views.user_login, name='login'),
    url(r'^playground/$', views.playground, name='playground'),
    url(r'^logout/$', views.user_logout, name='logouts')
]
