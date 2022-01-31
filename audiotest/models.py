from django.db import models
from django.utils import timezone
import datetime as dt
# Create your models here.

class VideoSave(models.Model):
    x = dt.datetime.now()
    create_time = models.DateTimeField()
    video = models.ImageField(upload_to= f'{str(x.date)}/', default= f'{str(x.hour)}_{str(x.minute)}.mp4')