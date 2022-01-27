from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL, null=True,related_name='comment')
    #article은 우리가 개별적으로 받아줘야함. 그래서 commentapp/create.html에서 form을 만들어서 받음
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='comment')
    #이름이 중복되어있는 부분에 대해 추가설명을 달 것

    content = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now=True)