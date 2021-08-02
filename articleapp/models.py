from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)

    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True) #프로필 미이더만들었음 //게시글 관련사진은 아티클
    content = models.TextField(null=True)  #testfield 긴텍스트

    created_at = models.DateField(auto_now_add=True, null=True)  #언제 작성된것인지 db자체적으로 저장될때 자동으로 할당해줘라