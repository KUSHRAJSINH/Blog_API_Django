from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend  # For filtering
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from .permissions import IsOwnerOrReadOnly  # Custom permission for ownership control

# 📌 View for Listing & Creating Posts (Filtering by Author Added)
class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]  # Enable filtering
    filterset_fields = ['author__username']  # Allow filtering by author's username

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)  # Set logged-in user as author

# 📌 View for Retrieving, Updating & Deleting a Single Post (Only Author Can Edit/Delete)
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# 📌 View for Listing & Creating Comments (Tied to a Specific Post)
class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set logged-in user as comment author

# 📌 View for Retrieving, Updating & Deleting a Single Comment (Only Author Can Edit/Delete)
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
