from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        profile = Profile.objects.get(pk=kwargs['pk'])
        #우리가 urls.py에서 pk로 받은 값들을 profile로 주는 것임
        if not profile.user == request.user:
            #pk로 받은 값이, 실제로 request를 보낸user와 동일한지를 확인해줌
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated


