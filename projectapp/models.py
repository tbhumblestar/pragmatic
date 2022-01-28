from django.db import models

class Project(models.Model):
    image = models.ImageField(upload_to='project/', null=False)
    #image를 올리면 media/project/ 에 upload됨
    title = models.CharField(max_length=25, null=False)
    description = models.CharField(max_length =25, null = True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} : {self.title}'
    #해당 클래스로부터 글이 출력이 될때, pk : title 과 같은 방식으로 출력이 됨
