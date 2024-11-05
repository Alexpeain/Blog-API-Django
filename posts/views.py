# posts/views.py

from rest_framework import generics
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer,UserSerializer
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .filters import PostFilter


class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all().order_by('created_at')
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend] 
    filterset_class = PostFilter
    
class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer

# class PostViewSet(generics.ListCreateAPIView):
#     permission_classes =(IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes =(IsAuthorOrReadOnly,)
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
    
# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
    
# class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer