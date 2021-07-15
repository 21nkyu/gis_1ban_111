from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import HelloWorld


def hello_world(request):

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













# logic

class AccountCreateView(CreateView):        #createview 상속
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') #class에서는 reverse_lazy를 사용한다. (reverse와 같다)
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'#페이지 가 있어야한다 routing - urls.py