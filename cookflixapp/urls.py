from django.conf.urls import url, include
from cookflixapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'cookflixapp'
urlpatterns = [
    url(r'^$', views.home, name='home'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
