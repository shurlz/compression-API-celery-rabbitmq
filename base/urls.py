from django.urls import path
from base.views import upload_image, download_image


urlpatterns = [
    path('upload/', upload_image),
    path('download/<str:item_id>/', download_image),
]