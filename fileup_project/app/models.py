from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Upload(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=20,default='tile')
    Upload_File=models.FileField(upload_to='files',blank=True)
    Upload_Image=models.ImageField(upload_to='images',blank=True)
    uploaded_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.title + '\n' + self.description

# Create your models here.
