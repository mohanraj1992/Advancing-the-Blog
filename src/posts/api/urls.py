from django.conf.urls import url
from django.contrib import admin

from .views import (
	RetrieveListAPIView,
	PostListAPIView
	)

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
    # url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', RetrieveListAPIView.as_view(), name='detail'), #for this we can try hitting with "http://localhost:8000/api/posts/new-post-2/" here new-post-2 is slug name
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
