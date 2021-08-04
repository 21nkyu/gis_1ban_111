from django.http import HttpResponseForbidden

from articleapp.models import Article


def article_ownership_required(func):   #함수를 받아서 함수를 꾸며줌 특이하점 새로운 함수를 안에 선언해준다
    def decorated(request, *args, **kwargs): #request인자를 받았고 정보를 받아서 확정되었고 글쓴이를 찾아야함
        target_article = Article.objects.get(pk=kwargs['pk']) #주소창에서 넘겨받은 pk를 가지고 있는 유저의 pk를 받는다?
        if target_article.writer == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated       #내부함수를 리턴 하면서 데코레이터를 끝낸다,  왜?