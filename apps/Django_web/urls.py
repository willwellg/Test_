from django.conf.urls import url
from Django_web.views import ArticleListView, ArticleDetailView
from . import views

urlpatterns = [
    # url(r'^$', views.index, name = 'index'),
    url(r'^$', ArticleListView.as_view(), name= 'Article'),
    url(r'^article/(?P<pk>[0-9]+)/$', ArticleDetailView.as_view(), name='article_detail'),
]