from django.conf.urls import include, url

import project.blog.urls


urlpatterns = [
    url('', include(project.blog.urls, namespace='project')),
]
