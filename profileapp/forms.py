from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta: #이 데이터는 아니지만 이것을 설명해주는 정보들
        model = Profile
        fields = ['image', 'nickname', 'message'] #user는 서버에서 처리해주기 때문에 받지 않는다.