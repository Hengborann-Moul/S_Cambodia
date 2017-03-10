from django.conf.urls import url

from sport_user import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^playground/$', views.playground, name='playground'),
    url(r'^user_logout/$', views.user_logout, name='user_logout')
]
