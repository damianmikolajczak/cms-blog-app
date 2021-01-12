from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('index', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='entire_post'),
    url('contact', views.Contact)

]
