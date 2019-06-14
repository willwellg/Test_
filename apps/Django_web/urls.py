from django.conf.urls import url
from Django_web.views import ArticleListView
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^home/$', views.home, name = 'home'),
    url(r'^query/$', views.queryAll, name = 'query'),
    url(r'^delete/$', views.delByID, name = 'delete'),
    url(r'^beginadd/$', views.addByID, name = 'beginadd'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^update/$', views.updateByID, name = 'update'),
    url(r'^first_page/$', views.first_page, name = 'first_page'),
]