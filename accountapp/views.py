from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm
# from accountapp.models import HelloWorld

# has_ownership = [account_ownership_required, login_required]
from articleapp.models import Article

#필요없는 부분인긴한데, 나중에 공부를 위해 남겨둠
# @login_required #login이 되어있는지 안되어있는지를 확인해줌
# def hello_world(request):
#     if request.method == "POST":
#         temp = request.POST.get("hello_world_input")#hello_world.html에서 받은 것
#
#         new_hello_world = HelloWorld() #HelloWorld()는 models.py에서 들고온 클래스(db)임
#         new_hello_world.text = temp
#         new_hello_world.save() #temp로 받은 hello_world_input를 db에 저장하는 거임
#         #이렇게 하면 db에 저장하는 것임
#
#         hello_world_list = HelloWorld.objects.all()
#         #objects.all : DB에 저장된 모든걸 다 긁어옴
#
#         return HttpResponseRedirect(reverse('accountapp:hello_world'))
#         #redirect를 return함. > redirect로 접근시 get메소드로 접속하게 됨 . 즉 post로 요청받은 작업을 끝내자마자 바로 get메소드로 다시 요청을 하게하는 것임. 이렇게 안하면 새로고침시, post명령이 계속 반복되어서 조질 수도 있음
#         #reverse는 urls.py에서 선언해준 app_name / path의 name을 통해서 좀 더 편하게 접근할 수 있도록 해줌 > 원래라면 'accountapp/hello_world.html' 이런식으로 접근해야 했을 것임
#
#     else:
#         hello_world_list = HelloWorld.objects.all()  # objects.all : 모든걸 다 긁어옴
#         return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
#         #context는 추가적인 데이터꾸러미임\



class AccountCreateView(CreateView):
    model = User
    # 장고에서 기본제공해주는 ,user라는 모델을 사용

    form_class = UserCreationForm
    #장고에서 기본적으로 제공해주는, 계정 생성을 위한 '폼'. 템플릿이 아님!!

    success_url = reverse_lazy('home')
    #함수형과는 다르게, 클래스에서는 reverse_lazy를 사용해야 함

    template_name = 'accountapp/create.html'
    #회원가입을 할때, 볼 html


#method_decorator : 일반 function에 쓸 수 있는 데코레이터를 메소드에 사용할 수 있게 변환
#기존에 있던 인증과정을 메소드데코레이터가 대신해줌
#views_decorator not used에 원래 함수를 만들어서 적용한 방식이 존재함


class AccountDetailView(DetailView, MultipleObjectMixin):#Detailview > readview
    model = User
    context_object_name = 'target_user'
    #context_object_name은 장고에서 제공하는 기능으로, context_object_name에 문자열을 할당하면
    # 그 문자열에 객체가 할당이 되며, 따라서 해당 문자열로(여기서는 'target_user')html파일에서 간편하게 접근이 가능함
    #즉 context_object_name은 뷰에서 템플릿 파일에 전달하는 컨텍스트 변수명을 전달함
    #그래서 context_object는 그냥 가독성을 위한 장치.. 라는 이야기가 잇음
    #실제로, AccountDetailView에 의해 실행되는 바로 밑의 accountapp/detail.html에서 target_user를 통해 유저정보를 접근함
    #그러면, 도대체 어떤 것들이 전달이 되는지????? user와 같은 원리인가?

    template_name = 'accountapp/detail.html'
    #detailview는 그냥 어떤 모델을쓸지, 그리고 어떤 템플릿을 사용해서 시각화해줄지 정도만 정해주면됨

    paginate_by = 12
    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(writer=self.get_object())
        return super(AccountDetailView, self).get_context_data(object_list=object_list, **kwargs)


@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountUpdateView(UpdateView): #create view와 매우 유사
    model = User
    # 장고에서 기본제공해주는 ,user라는 모델을 사용

    form_class = AccountUpdateForm
    #장고에서 기본적으로 제공해주는, 계정 생성을 위한 '폼'. 템플릿이 아님!!

    success_url = reverse_lazy('home')
    #함수형과는 다르게, 클래스에서는 reverse_lazy를 사용해야 함
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html'
    #회원가입을 할때, 볼 html

@method_decorator(account_ownership_required, 'get')
@method_decorator(account_ownership_required, 'post')
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
    context_object_name = 'target_user'


