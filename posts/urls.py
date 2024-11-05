# posts/urls.py

from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet,UserViewSet  #PostDetailView,UserList, UserDetail,
# router = DefaultRouter()
# router.register(r'posts', PostViewSet)
router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")
urlpatterns = router.urls

