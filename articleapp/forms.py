from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        #model에서 만든 field들 중 일부
        #model에서 foreignkey로 project와 writer를 묶어놨기때문에
        #form에서 필처처럼 project가 나옴옴