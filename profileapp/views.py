from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

@method_decorator(login_required, 'get')  #@method_decorator(login_required(login_url=), 'get')
@method_decorator(login_required, 'post')

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name = 'target_profile'  #프로필이기때문에 이름을 이렇게 // 접근 할때 이 이름으로 접근한다
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'