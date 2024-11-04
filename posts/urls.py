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
# urlpatterns = [
#     # path('', include(router.urls)),
#     path("users/", UserList.as_view()), # new
#     path("users/<int:pk>/", UserDetail.as_view()),
#     path('posts/', PostViewSet.as_view(), name='post-list'),
#     path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
# ]
