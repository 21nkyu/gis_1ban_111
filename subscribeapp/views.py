from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from projectapp.models import Project
from subscribeapp.models import Subscription
#유저를 특정하기 위해서는 로그인 돼있어야한다


@method_decorator(login_required, 'get') #get만 사용함
class SubscriptionView(RedirectView):

    def get(self, request, *args, **kwargs):
        user = request.user
        project = Project.objects.get(pk=kwargs['project_pk'])#어떤 프로젝트 인지 알아야한다 겟 단일객체를 가져오는 피케이가 키워다 아그먼츠에 들어있는 프로젝트 피케이를 찾아낼것이다 구독정보를 누른 게시판

        subscription = Subscription.objects.filter(user=user,
                                                   project=project)   #두가지 모두 만족하는 구독정보를 찾는다

        #분기 구독정보가 있으면 구독 해제 //없었다면 구독을 새로 생성
        if subscription.exists():
            subscription.delete()
        else:
            Subscription(user=user, project=project).save()  #바로 만들자 마자 save하는 것으로 축약을 했음

        return super().get(request, *args, **kwargs)
        # ㅗhttp get  방싱ㄱ으로 박았을때 어떻게 동작할지

    # 우리는리다이렉트 뷰를 상속받아서 만든다 그래서 완성을 하면 어디로 갈지를 정해줘야 한다
    # 그래서 get redirect url을 연결해준다
    def get_redirect_url(self, *args, **kwargs):
        return reverse('projectapp:detail', kwargs={'pk': kwargs['project_pk']}) #넘겨 받은 pk 는 project_pk