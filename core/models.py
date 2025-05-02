from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title