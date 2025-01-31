from django.urls import path
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .views import PostListCreateView, PostDetailView, CommentListCreateView, CommentDetailView

@api_view(['GET'])
def api_root(request):
    return Response({
        "posts": "/api/posts/",
        "comments": "/api/comments/",
        "token_obtain": "/api/token/",
        "token_refresh": "/api/token/refresh/"
    })

urlpatterns = [
    path('', api_root, name='api-root'),  # ✅ Add a default API root
    path('posts/', PostListCreateView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]
