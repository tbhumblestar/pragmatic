from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='subscription')
    project = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='subscription')
    # 어떤 유저와 프로젝트가 쌍이되도록 할 것임
    # Subscription모델(DB)에 user라는 속성은 User객체와의 foreignkey
    # Subscription모델(DB)에 project라는 속성은 ProjectDB와의 foreignkey임
    # 그러면 결국, User와 Project가 묶이는 거임(쌍이 되는 거임)

    class Meta:
        unique_together = ('user', 'project')
    #user와 project가 갖는 쌍이 오직 하나만 있도록 해주는 것임

