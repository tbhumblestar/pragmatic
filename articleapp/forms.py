from django import forms
from django.forms import ModelForm

from articleapp.models import Article
from projectapp.models import Project


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class':'editable text-start','style':'height:auto;'}))
    #뭘 미디엄에디터로 만들어줄지에 대한 정보를 주는 것
    #이렇게 넣어주면, content 필드가 만들어질때, html태그의 class와 style속성을 미리 결정해주는 것임

    #프로젝트를 고르지 않아도 article을 작성할 수 있도록 하기 위함
    project = forms.ModelChoiceField(queryset=Project.objects.all(),required=False)
    #queryset=Project.objects.all() : project들이 전부다 나오도록 하는 것임

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']
        #model에서 만든 field들 중 일부
        #model에서 foreignkey로 project와 writer를 묶어놨기때문에 form에서 project를 선택하는 부분이 필터처럼 나옴