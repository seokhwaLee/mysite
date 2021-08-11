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
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date' #필드 정렬 기준
    was_published_recently.boolean = True #True False가 글자가 아니라 아이콘으로 보여짐
    was_published_recently.short_description = 'Published recently?' #Title을 변경시켜줌


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  #선택지에 해당하는 질문
    choice_text = models.CharField(max_length=200) #문자
    votes = models.IntegerField(default=0)  #투표수 : 숫자

    def __str__(self):
        return self.choice_text