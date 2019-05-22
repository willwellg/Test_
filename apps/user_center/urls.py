from django.conf.urls import include, url
from . import views

urlpatterns = (
    url(r'login', views.Login, name = 'login'),
    url(r'search', views.Search, name = 'search'),
    url(r'add', views.Add, name = 'add'),
    url(r'register', views.Register, name = 'register'),
    url(r'logout', views.Logout, name = 'logout'),

)