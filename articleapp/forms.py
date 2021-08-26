from django import forms
from django.forms import ModelForm

from articleapp.models import Article


class ArticleCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable',
                                                           'style': 'text-align:left;'
                                                                    'min-height:10rem;'})) #우리가 케릭터필드를 커스텀 해줘야한다  모델.이미지필드.... 폼에서는 폼.케릭터필드 지정해준다
    # 캐릭터필드가 어떤형식으로 나올지 위젯을 지정해줘야한다 # 커스텀 하는 이유는 에디터블이라는 클래스를 만들어주기 위해서 태ㅔㅐ스트 에어리어 속성에 클래스를 에디터블아라고 설정을 해준다

    class Meta:
        model = Article
        fields = ['title', 'image', 'project', 'content']