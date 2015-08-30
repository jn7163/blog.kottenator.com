from django.conf.urls import include, url

urlpatterns = [
    url('', include('blog.urls')),
]
