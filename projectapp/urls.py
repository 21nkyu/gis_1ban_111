from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView

app_name = 'projectapp' #reverse(projcetapp 에 사용하기 위해서

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),

]