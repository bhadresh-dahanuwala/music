from django.urls import path
from .views import UploadAudioForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload_audio/', UploadAudioForm, name='upload_audio')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)