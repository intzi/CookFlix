from django.conf.urls import url, include
from django.contrib import admin
from cookflixapp import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^register/$', views.register, name='register'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'browse/(?P<id>\d+)/$', views.recipe, name='recipe'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^search/$', views.search, name='search'),

]
