from django.conf.urls import url, include
from cookflixapp import views

app_name = 'cookflixapp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]