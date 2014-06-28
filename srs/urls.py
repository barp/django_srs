from django.conf.urls import url

from srs import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
]