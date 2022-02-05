from django.db import models
from django.utils import timezone
import datetime as dt


class QuestionChar(models.Model):
    question_text = models.CharField(max_length=200)
    question_num = models.CharField(max_length=200)
    question_cla = models.CharField(max_length=200)
    question_dif = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=timezone.now)

    def __str__(self):
        return self.question_text

class InterviewStorage(models.Model):
    subject = models.CharField(max_length=200, default=str(dt.datetime.now().strftime("%Y년-%m월-%d일-%H시-%M분-%S초")))
    interview_video = models.FileField(upload_to='%Y_%m_%d')
    create_time = models.DateTimeField()

    def __str__(self):
        return self.subject
# Create your models here.
