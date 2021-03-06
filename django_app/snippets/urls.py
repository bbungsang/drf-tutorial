from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from snippets import views

urlpatterns = [
    # fbv urls
    # url(r'^snippets/$', views.snippet_list, name='snippet_list'),
    # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail, name='snippet_detail'),

    # cbv urls
    url(r'^snippets/$', views.SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)