from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import RedirectView

from articleapp.models import Article
from likeapp.models import LikeRecord


@method_decorator(login_required, 'get')
class LikeArticleView(RedirectView): #구독앱을 만들면서 사용함

    def get(self, request, *args, **kwargs):  #get이라는 메서드를 오버라이드 해서
        user = request.user
        article = Article.objects.get(pk=kwargs['article_pk'])  #단일객체 get 주소창에서 kwargs 안에서 articl_pk

        likeRecord = LikeRecord.objects.filter(user=user,
                                               article=article)
        if likeRecord.exists():
            #좋아요 반영X
            messages.add_message(request, messages.ERROR, '좋아요는 한번만 가능합니다.')#get인자를 그대로 넘겨주고 , 원하는 level을 , 원하는 메세지
            return HttpResponseRedirect(reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']}))
            # 좋아요 기록이 존재 한다면 좋아요를 찍은 게시글로 다시 되돌아가게 된다
        else:
            LikeRecord(user=user, article=article).save()

        article.like += 1
        article.save()
        #좋아요 반영
        messages.add_message(request, messages.SUCCESS, '좋아요가 반영되었습니다')
        return super().get(request, *args, **kwargs)

    def get_redirect_url(self, *args, **kwargs):  #리턴을 하고 어디로 갈건지
        return reverse('articleapp:detail', kwargs={'pk': kwargs['article_pk']})