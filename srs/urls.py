from django.conf.urls import url

from srs import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^deck/(?P<pk>[0-9]+)/$', views.DeckView.as_view(), name='deck'),
]