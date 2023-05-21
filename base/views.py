from base.forms import UploadForm
from base.models import UploadModel
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpResponse
from base.tasks import compress_image_background



@api_view(['POST'])
def upload_image(request) -> 'JsonResponse':

    form = UploadForm(request.data, request.FILES)

    if not form.is_valid():
        return JsonResponse(form.errors)
    
    instance: UploadModel = form.save()

    compress_image_background.apply_async(( instance.id, ))

    return JsonResponse({
        'message': 'File Received, Youd Get A Download Link Of The Compressed Version'
        })



@api_view(['GET'])
def download_image(request, item_id):
    try:
        _instance: UploadModel = UploadModel.objects.get(id = item_id)
        _path = _instance.compressed_image_path
        _name = _path.split('/')[-1]
    except:
        return JsonResponse({ 'message': 'File Not Found' })

    image = open(f'{_path}', 'rb')

    response = HttpResponse(image, content_type='image/*')
    response['Content-Disposition'] = f'attachment; filename="{_name}"'
    return response
