from django.conf.urls import url
from Django_web.views import ArticleListView
from . import views

urlpatterns = [
    # url(r'^$', views.index, name = 'index'),
    url(r'^$', ArticleListView.as_view(), name= 'Article'),
]