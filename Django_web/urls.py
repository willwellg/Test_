from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^query/$', views.queryAll, name = 'query'),
    url(r'^delete/$', views.delByID, name = 'delete'),
    url(r'^beginadd/$', views.addByID, name = 'beginadd'),
    url(r'^add/$', views.add, name = 'add'),
    url(r'^update/$', views.updateByID, name = 'update'),
    url(r'^upload/$', views.uploade, name = 'upload'),
    url(r'^upload_excel$', views.upload_excel, name = 'upload_excel'),
    url(r'^first_page/$', views.first_page, name = 'first_page'),
    #添加一行注释
]