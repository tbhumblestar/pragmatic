from django.db import models

# Create your models here.

class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)
    #null = True이면, 이 text의 데이터들 중 빈게 있어도 된다 이말임. False면 필수