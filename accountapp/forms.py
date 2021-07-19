
#usercreationform 을 상속을 받아 커스터마이징 할것임
from django.contrib.auth.forms import UserCreationForm


class AccountCreationForm(UserCreationForm): #오버라이딩을 한다 accountcreationform == usercreationform Acc~~가 usercreaform을 상속한다.
    def __init__(self, *args, **kwargs):        #부모의 init를 상속
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True   #id = username (database),  user 라는 field를 못쓰게 하겠다