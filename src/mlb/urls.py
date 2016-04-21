from django.conf.urls import include, url

urlpatterns = [
    url('', include('mlb.blog.urls')),
]
