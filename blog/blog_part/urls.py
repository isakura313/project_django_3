from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog_part'
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:post>', views.post_detail, name = 'post_detail'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)