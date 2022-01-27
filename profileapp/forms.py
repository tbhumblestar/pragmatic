from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']


#원래라면, 각 모델들의 데이터종류 대해 새로운 폼을 만들어야 함
#근데 지금이야 괜찮지만, 데이터가 존나많을수도 잇음
#그런 경우를 대비해서 위의 코드와 같은 방식으로,즉 modelform을 상속받는 방식으로 쉽게 만들 수 있음
