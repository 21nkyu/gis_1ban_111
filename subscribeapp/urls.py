from django.urls import path

from subscribeapp.views import SubscriptionView

app_name = 'subscribeapp'

urlpatterns = [
    path('subscribe/<int:project_pk>', SubscriptionView.as_view(), name='subscribe') #구독정보를 어느 구독정보를 날려줄것인지

]

# {% url 'subscribeapp앱네임 에서 온것:subscribe 네임에서 온 것' project_pk=target_project.pk %}"