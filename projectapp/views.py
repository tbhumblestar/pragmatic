from django.urls import reverse
from django.views.generic import CreateView, ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from articleapp.models import Article
from projectapp.forms import ProjectCreationForm
from projectapp.models import Project
from subscribeapp.models import Subscription


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    template_name = 'projectapp/create.html'

    def get_success_url(self):
        return reverse('projectapp:detail',kwargs={'pk':self.object.pk})


class ProjectDetailView(DetailView, MultipleObjectMixin):
    #MultipleObjectMixin : 여러가지 오브젝트를 더할 수 있게 해줌
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'

    paginate_by = 25

    def get_context_data(self, **kwargs):
        object_list = Article.objects.filter(project=self.get_object())
        #Article안의 object에 대해서 filter를 적용.
        #필터내용이 self의 get_object()와 동일한녀석

        project = self.object
        user = self.request.user
        if user.is_authenticated:
            subscription = Subscription.objects.filter(user=user,project=project)

        return super(ProjectDetailView, self).get_context_data(object_list=object_list,subscription=subscription, **kwargs)
        #obejct_list라는 객체를 활용해 필터링을 시켜준 것임임
        #결과적으로 필터링된 object_list라는 놈을 html랜더링할때, 그 html에 같이 던져줌
        #추가로 user가 로그인되어 있다면, 조건에 맞는(filter과정을 거친)subscription정보를 같이 던져줌



class ProjectListView(ListView):
    model = Project
    context_object_name = 'project_list'
    template_name = 'projectapp/list.html'
    paginate_by = 5
