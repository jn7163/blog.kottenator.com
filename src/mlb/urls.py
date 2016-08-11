from django.conf.urls import include, url

import mlb.blog.urls


urlpatterns = [
    url('', include(mlb.blog.urls, namespace='blog')),
]
