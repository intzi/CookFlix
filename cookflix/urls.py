from django.conf.urls import url, include
from django.contrib import admin
from cookflixapp import views

urlpatterns = [
    url(r'^$', include('cookflixapp.urls')),
    url(r'^about/', views.about, name='about'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/',views.login, name='login'),
    url(r'^signup/', views.signup, name='signup'),
    url(r'^register/', views.register, name='register'),
]