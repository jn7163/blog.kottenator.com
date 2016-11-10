from django.conf.urls import url

import project.blog.views


urlpatterns = [
    url(r'^$', project.blog.views.articles, name='articles'),
]
