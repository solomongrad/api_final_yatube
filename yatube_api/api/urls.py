from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

v1_router = SimpleRouter()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register('follow', FollowViewSet, basename='follow')
v1_router.register('groups', GroupViewSet)
v1_router.register(r'^posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/', include('djoser.urls.jwt')),
]
