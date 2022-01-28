from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

#이 이름을 설정해두면 나중에 어떤 함수를 활용해서 쉽게 접근이 가능함
#즉,개발과정에서 ("127.0.0.1:8000/acount/hello_world.html")이런식으로 접근안해도되고(너무 귀찮)
#hello_world라는 이름을 가진 앱으로 바로가라! 라고 명렬할 수 있음.
# 그러기위해 appname과 밑의 path의 name이 필요함





urlpatterns = [


    path('login/', LoginView.as_view(template_name="accountapp/login.html"), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #클래스는 끝에 .as_view()를 붙여줘야 함수형처럼 작동을 함

    path('create/', AccountCreateView.as_view(), name='create'),

    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    #url로 받은 정보중 detail/뒤의 부분을, pk라는 이름의 int(integer-정수)정보로 받겠다! 라는 것임
    #이렇게 받은 정보는 AccountDetailView 얘를 통해서 랜더링 되는 템플릿에 넘어감
    #pk = primary key : 유저를 식별하는 유저고유의 키

    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    #url로 받은 정보중 update/뒤의 부분을, pk라는 이름의 int(integer-정수)정보로 받겠다! 라는 것임
    #이렇게 받은 정보는 AccountUpdateView 얘를 통해서 랜더링 되는 템플릿에 넘어감

    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),

]
#path경로로 들어오면, 그다음 인자인 view의 def/class를 사용해라.