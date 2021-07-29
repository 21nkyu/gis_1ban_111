from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'  #적어야 아티클 앱으로 갈때 역산한다.

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list')

]

# path 첫번째 들어갈 주소 /, 로직 클래스베이스드 뷰 as뷰