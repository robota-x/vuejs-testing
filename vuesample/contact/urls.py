from django.conf.urls import url

from . import views

app_name = 'contact'
urlpatterns = [
    url(r'^offices/(?P<id>[0-9])$', views.office, name='office_details'),
    url(r'^offices$', views.office, name='office_list'),
    url(r'^$', views.index, name='index'),
]
