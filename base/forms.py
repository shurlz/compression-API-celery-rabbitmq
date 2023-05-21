from base.models import UploadModel
from django.forms import ModelForm


class UploadForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta:
        model = UploadModel
        fields = '__all__'
