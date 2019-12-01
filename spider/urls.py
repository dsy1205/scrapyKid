from django.conf.urls import url
from spider import views

urlpatterns = [
    url('index/', views.index),
    url('\d+/$', views.index)
]
