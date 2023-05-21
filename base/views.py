from base.forms import UploadForm
from rest_framework.decorators import api_view
from django.http import JsonResponse
from base.tasks import compress_image_background



@api_view(['POST'])
def upload_video(request) -> 'JsonResponse':

    form = UploadForm(request.data, request.FILES)

    if not form.is_valid():
        return JsonResponse(form.errors)
    
    instance = form.save()

    compress_image_background.apply_async(( instance.id, ))

    return JsonResponse({
        'message': 'File Received, Youd Get A Download Link Of The Compressed Version'
        })
