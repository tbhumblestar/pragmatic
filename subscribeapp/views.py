from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView, ListView

from articleapp.models import Article
from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
        #project_pk를 get방식으로 받아서, detail/pk로 이동하게 하는것
        #url로 이동할 때, get방식으로 정보를 받을 것임
    #   #get메소드로, 해당 url로 redirect

    def get(self, request, *args, **kwargs):
        #get요청이 들어올 경우 자동으로 수행됨 즉 get메소드로 들어올 경우에 얘가 무조건 사용된다.
        #>get이 들어오면 얘가 수행되고 그후에, get_redirect_url이 수행되는 것임

        project = get_object_or_404(Project,pk=self.request.GET.get('project_pk'))
        #project_pk를 가지고 있는 Project를 찾는데, 만약 그게 없다면 404(페이지를 찾을 수 없다)를 돌려주도록 한 것
        user = self.request.user

        subscription = Subscription.objects.filter(user=user, project=project)
        #유저와 project사이의 subscription이 있는지 없는지 확인을 위함

        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()

        return super(SubscriptionView, self).get(request,*args,**kwargs)

@method_decorator(login_required,'get')
class SubscriptionListView(ListView):
    model = Article
    context_object_name = 'article_list'
    template_name = 'subscribeapp/list.html'
    paginate_by = 5

    def get_queryset(self):#가지고 오는 게시글들을 필터링할 수 있음
        projects = Subscription.objects.filter(user=self.request.user).values_list('project')
        #Subscription의 object들 중, user = 요청한 유저인 object들의 project값을 리스트로 만들어라(value_list)
        article_list = Article.objects.filter(project__in=projects)
        #project값이 projects안에 들어있는 Article의 object들을 들고와라
        return article_list