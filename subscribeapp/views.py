from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription


@method_decorator(login_required,'get')
class SubscriptionView(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': self.request.GET.get('project_pk')})
        #project_pk를 get방식으로 받아서, detail/pk로 이동하게 하는것
        #url로 이동할 때, get방식으로 정보를 받을 것임

    def get(self, request, *args, **kwargs):
        #겟 메소드가 사용될떄 발동되는 애임
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

