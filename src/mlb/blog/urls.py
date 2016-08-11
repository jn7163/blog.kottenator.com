from django.conf.urls import url

import mlb.blog.views


urlpatterns = [
    url(r'^$', mlb.blog.views.articles, name='articles'),
]
