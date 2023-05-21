from django.db.models import Q
from compressor.celery import app
from base.models import UploadModel
from base.utils.send_mail import send_email



@app.task
def compress_image_background(new_instance_id: int):
    from base.utils.compress_image import compress_image
    
    new_instance = UploadModel.objects.get(id = new_instance_id)

    compress_image(instance = new_instance)



@app.task
def send_confirmations():
    
    # fetch all processed images but emails havent been sent to owners

    for instance in UploadModel.objects.filter(
        Q(sent_confirmation=False) &
        Q(is_compressed=True)
        ):

        # try sending email, if un-sucessful, task picks it up again next time

        try:
            """ 
            insert your email sending method here 
            
            send_email(
                to = instance.email, 
                subject = 'Your Image Has Been Compressed Successfully',
                message = f'Click this link to download your image: '
                       )
                       
            """
            
            # update task status in the database
            instance.sent_confirmation = True
            instance.save()
        except:
            pass