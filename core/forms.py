from django import forms
from .models import Video
from django.core.exceptions import ValidationError
import mimetypes

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

    def clean_video_file(self):
        file = self.cleaned_data.get('video_file')
        if file:
            mime_type, _ = mimetypes.guess_type(file.name)
            if not mime_type or not mime_type.startswith('video'):
                raise ValidationError('Only video files are allowed.')
        return file