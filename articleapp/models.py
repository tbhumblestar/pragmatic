from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,related_name='article', null=True)
    #User가 회원탈퇴등을 했을 때, 게시글이 사라지는 것이 아니라 알 수 없음이 되도록 설정을 하겠다.
    #related_name은 User객체에서 article에 접근할때 쓰는 이름. 이렇게 해두면 User.article과 같은 방식으로 writer에 접근가능
    #set_null를 했으니 null값에 대해 적어줘야 함 > null=True

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/',null=False)
    #null=Flase > 이미지가 반드시 있어야 함
    content = models.TextField(null=True)
    #Textfield는 CharField에 비해 길때 사용

    created_at = models.DateField(auto_created=True,null = True)\
    #자동으로 완성됨
