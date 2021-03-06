from django.conf.urls import url, include
from django.contrib import admin
from cookflixapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^about/', views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^browse/$', views.browse, name='browse'),
    url(r'^browse/(?P<cuisine_type>[\w\-]+)/$', views.browse, name='browse'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'recipe/(?P<id>\d+)/$', views.recipe, name='recipe'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^profile/(?P<username>[\w\-]+)/$', views.profile, name='profile'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url(r'^(?P<username>[\w\-]+)/myrecipes/$', views.myrecipes, name='myrecipes'),
    url(r'^browse/(?P<id>[\d]+)', views.delete_post, name='delete_post'),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
