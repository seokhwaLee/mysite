import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)  #질문내용 : 문자, 최대길이 200
    pub_date = models.DateTimeField('date published')  #생성날짜 : 시간 타입

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #선택지에 해당하는 질문
    choice_text = models.CharField(max_length=200) #문자
    votes = models.IntegerField(default=0)  #투표수 : 숫자

    def __str__(self):
        return self.choice_text