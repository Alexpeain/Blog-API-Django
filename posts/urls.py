# posts/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet,PostDetailView

# router = DefaultRouter()
# router.register(r'posts', PostViewSet)

urlpatterns = [
    # path('', include(router.urls)),
    path('posts/', PostViewSet.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
]
