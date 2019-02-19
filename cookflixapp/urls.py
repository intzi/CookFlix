from django.conf.urls import url, include
from cookflixapp import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
]
