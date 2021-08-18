from django.contrib.auth.decorators import login_required
# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, ListView

from projectapp.forms import ProjectCreationForm
from projectapp.models import Project


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreationForm
    success_url = reverse_lazy('articleapp:list')#디테일뷰가 없으니 임시로
    template_name = 'projectapp/create.html' #에서 시각화 할거다

    def get_success_url(self):
        return reverse('projectapp:detail', kwargs={'pk': self.object.pk}) #완성되면 가는 화면


class ProjectDetailView(DetailView):
    model = Project
    context_object_name = 'target_project'
    template_name = 'projectapp/detail.html'


class ProjectListView(ListView):
    model = Project
    template_name = 'projectapp/list.html'
    paginate_by = 20