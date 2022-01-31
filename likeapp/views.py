from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord

@transaction.atomic
#이 데코레이터를 받는 함수의안의 모든 작용이 transaction으로 이루어짐(전부다 성공해야만 함. 일부성공이 X)
def db_transaction(user,article):

    article.like += 1
    article.save()
    #transaction으로 묶임 > 여기서 +1 된 후, save했다해도, 뒤에서 좋아요가 exist라 실행이 안된다면, 여기서 +1 후 save된것도 취소가 됨

    if LikeRecord.objects.filter(user=user, article=article).exists():
        # LikeRecord에 user와 article이 각각 위에서 설정한 user와 article인 LikeRecord가 존재하는지?
        # 있으면 이미 좋아요를 찍은 사람임
        article.save()
        # 장고의 메세지기능
        # request / 메세지레벨 / 메세지내용을 인자로 넣어줌
        raise ValidationError('Like already Exists!')

    else:
        LikeRecord(user=user, article=article).save()
        # likerecord에 조건에 맞는 값을 추가(저장)







@method_decorator(login_required,'get')
class LikeArticleView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('articleapp:detail', kwargs={'pk': kwargs['pk']})

    def get(self, *args, **kwargs):
        # get요청이 들어올 경우 자동으로 수행됨 즉 get메소드로 들어올 경우에 얘가 무조건 사용된다.
        # >get이 들어오면 얘가 수행되고 그후에, get_redirect_url이 수행되는 것임
        user = self.request.user
        article = get_object_or_404(Article,pk=kwargs['pk'])
        #pk값이 올바르게 존재하는 Article을 가져오고 없으면 404에러

        try:
            db_transaction(user, article)
            messages.add_message(self.request, messages.SUCCESS, "좋아요가 반영되었습니다!")
        except ValidationError:
            messages.add_message(self.request, messages.ERROR, '좋아요는 한번만 가능합니다')
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['pk']}))
            #db_transaction를 했다가 실패할 경우, 요청보낸 게시글로 돌아감


        return super(LikeArticleView,self).get(self.request, *args, **kwargs)