from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='like_record', null=False) #d연결유저가 삭제 되었을때 함께ㅐ 삭제 된다 cascade
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='like_record', null=False)
    #db단에 조건추가 한게시글에는 하나의 좋아요만 가능하도록
    # 유니크 하게 쌍으로 연결해준다
    class Meta:
        unique_together = ['user', 'article']