from django.conf.urls import url
from member import views

from django.conf.urls import include

urlpatterns = [
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

# 탐색 가능한 API 에 사용할 로그인 뷰를 추가할 수 있도록 한다.
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]