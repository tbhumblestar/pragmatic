from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #profile과 User객체를 하나씩 1대1로 연결해준다
    #on_delete : profile과 연결된 User객체가 사라질때 어떻게 할지
    #Cascade :  함꼐 사라진다
    #related_name : 얘를 통해 쉽게 접근이 가능

    image = models.ImageField(upload_to='profile/', null=True)
    #이거 미디어파일임. 그래서 settings.py에 적힌대로 앞에 'media/'부분이 추가됨
    # 즉, 'media/profile/~' 이런식으로 저장됨
    #null = True : 없어도 된다.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    #charfiled : 그냥 글자필드
    #unique = True : 고유해야함
    message = models.CharField(max_length=20,null = True)