from django.urls import path
from base.views import upload_video


urlpatterns = [
    path('', upload_video),
]