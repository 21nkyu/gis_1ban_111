from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def hello_world(request):
    if request.user.is_authenticated:#분기문 추가 is_authen 로그인여부 확인



        if request.method == 'POST':        #post get중 post로 오면

            temp = request.POST.get('hello_world_input')

            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))


        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html',
                          context={'hello_world_list': hello_world_list})
    else:
        return HttpResponseRedirect(reverse('accountapp:login'))













# logic

class AccountCreateView(CreateView):        #createview 상속
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #class에서는 reverse_lazy를 사용한다. (reverse와 같다)
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' #????
    template_name = 'accountapp/detail.html'#페이지 가 있어야한다 routing - urls.py

class AccountUpdateView(UpdateView):
    model = User                    #무엇을 업데이트 할 것인지
    form_class = AccountCreationForm   #1수정할 내용을 넣어준다. 따로 접근하지 않아도 됨 2커스터마이징을 해야함 상속 받아서
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')#일단은 헬로우월드
    template_name = 'accountapp/update.html'

    def get(self, request, *args, **kwargs):  #선택적 매개변수
        if request.user.is_authenticated and self.get_object() == request.user: #self =accountview의객체? 계정객체 get_object == target_user
            return super().get(request, *args, **kwargs) #부모의 get메서드를 그대로 실행해라
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):  #선택적 매개변수
        if request.user.is_authenticatedand and self.get_object() == request.user:
            return super().post(request, *args, **kwargs) #부모의 get메서드를 그대로 실행해라
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    #탈퇴 폼클래스 필요 없음.
    context_object_name = 'target_user' #어떻게 사용할지 어떤객체를 지울 것인지
    cuccess_url = reverse_lazy('accountapp:hello_world') #탈퇴 완료시 연결 url
    template_name = 'accountapp/delete.html' #어떤식으로 렌더링// urls.py에서 어떻게 접근할건지

    def get(self, request, *args, **kwargs):  #선택적 매개변수
        if request.user.is_authenticated and self.get_object() == request.user: #self =accountview의객체? 계정객체 get_object == target_user
            return super().get(request, *args, **kwargs) #부모의 get메서드를 그대로 실행해라
        else:
            return HttpResponseForbidden()

    def post(self, request, *args, **kwargs):  #선택적 매개변수
        if request.user.is_authenticatedand and self.get_object() == request.user:
            return super().post(request, *args, **kwargs) #부모의 get메서드를 그대로 실행해라
        else:
            return HttpResponseForbidden()