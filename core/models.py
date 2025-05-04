from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=200)
    video_file = models.FileField(upload_to='videos/')
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True, null=True, default='profile_pics/default.jpg')
    bio = models.TextField(max_length=250, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s profile"
