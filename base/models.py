from django.db import models


class UploadModel(models.Model):
    email = models.CharField(max_length=100)
    real_image = models.ImageField(upload_to='images')
    uploaded_on = models.DateTimeField(auto_now_add=True)
    is_compressed = models.BooleanField(default=False)
    sent_confirmation = models.BooleanField(default=False)
    compressed_image_path = models.CharField(max_length=9000, blank=True)

    class Meta:
        managed = True
        db_table = 'Upload'
        verbose_name_plural = 'Uploads'
        ordering = ['-uploaded_on']

    def __str__(self) -> str: 
        return self.email