import uuid
from compressor.settings import MEDIA_ROOT
from PIL import Image
from base.models import UploadModel



def compress_image(instance: 'UploadModel') -> None: 

    new_name = str(uuid.uuid4())

    image = Image.open(instance.real_image.path)

    new_img = image.convert('RGB')

    new_img.save(f'{MEDIA_ROOT}/{new_name}.jpg', optimize = True, quality = 10)

    instance.compressed_image_path = f'{MEDIA_ROOT}/{new_name}.jpg'
    instance.is_compressed = True
    instance.save()
