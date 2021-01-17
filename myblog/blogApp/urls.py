from . import views
from .models import Post
from django.urls import path, include
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'comments', views.CommentViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
    path('', views.PostList.as_view(), name='home'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='entire_post'),
    path('<slug:slug>/', views.post_detail, name='entire_post'),
    url('contact', views.Contact, name="contact"),
]
