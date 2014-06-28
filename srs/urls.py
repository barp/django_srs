from django.conf.urls import url

from srs import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
]