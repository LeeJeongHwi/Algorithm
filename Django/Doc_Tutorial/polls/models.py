import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub-date'
    #원칙적으로 임의의 메서드에 의한 값은 정렬 불가능 ->다른값 기준항목 정렬 -> 기준 항목을 설정하는 항목
    was_published_recently.boolean = True
    #값이 불리언 값 형태인지 설정(True로 하면 아이콘으로 나옴)
    was_published_recently.short_description = 'Published Recently?'
    #항목의 헤더이름 설정
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


# Create your models here.
