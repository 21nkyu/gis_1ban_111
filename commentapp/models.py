from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.SET_NULL,
                                related_name='comment', null=True)

    #작성한사람연결 일대일 연결이 아니다 연결하는건 유저
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='comment', null=True)

    #content  작문의 데이터 텍스트 필드 뭘 넣어야 만든다
    content = models.TextField(null=False)

    #auto 자동으로 생성해줌ㅇㅇㅇㅇㅇㅇㅇㅇ
    created_at = models.DateTimeField(auto_now_add=True)