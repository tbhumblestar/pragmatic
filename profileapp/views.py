from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    #accountapp때와는 다르게, 모델도 장고가 기본적으로 제공하는 User를 쓰는게 아니라
    #우리가 만든 Profile이라는 모델을사용
    form_class = ProfileCreationForm
    #우리가 만든 폼
    context_object_name = "target_profile"
    template_name = 'profileapp/create.html'
    #profileapp안의 template안의 profile안에 위치한 create.html임

    def form_valid(self, form):
        #profile의 model인 Profile을 보면, user / image / nickname / message 총 네개의 자료를 받지만,
        #form에서 보면 image/ nickname / message 총 세개의 데이터만 사용함
        #사용자가 그냥 지맘대로 user에 접속해서 이것저것 수정할까봐, user를 사용하지 않는 것임
        #근데 그러다보니까 user라는 데이터 정보가 없어서 문제가 발생함.
        #이를 해결하기 위해 , 지금 form_valid라는 애를 써주는 것임

        temp_profile = form.save(commit=False)
        # form에서 데이터를 보낼때, 그 데이터가 form에 들어가있음
        # form.save(commit = False) :form에서 보낸 데이터를 임시로 저장함
        temp_profile.user = self.request.user
        #유저정보를 self.request.user 즉 request를 보낸 user로 선언
        temp_profile.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
        #self.object = user임
        #profile.user 는 모델의 user임.
        #결론적으로 user의 pk를 넘겨줌

        #그렇게 해서, create가 success시 반환하는 url을
        #account:detail/<pk> 와 같은 식으로 보내줌.



@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView): #바로위의 create를 거의 가져옴
    model = Profile
    #accountapp때와는 다르게, 모델도 장고가 기본적으로 제공하는 User를 쓰는게 아니라
    #우리가 만든 Profile이라는 모델을사용
    context_object_name = "target_profile"
    form_class = ProfileCreationForm
    #우리가 만든 폼

    template_name = 'profileapp/update.html'
    #profileapp안의 template안의 profile안에 위치한 create.html임

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})
        #self.object = user임
        #profile.user 는 모델의 user임.
        #결론적으로 user의 pk를 넘겨줌

