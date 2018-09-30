from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^(?P<todo_id>[0-9]+)/done/$', views.done, name='done'),
    url(r'^(?P<todo_id>[0-9]+)/delete/$', views.delete, name='delete'),
]
