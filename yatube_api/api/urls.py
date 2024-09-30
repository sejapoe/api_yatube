from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, CommentViewSet, GroupViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register('groups', GroupViewSet)

nested_router = SimpleRouter()
nested_router.register('comments', CommentViewSet)

urlpatterns = [
    path('api-token-auth/', obtain_auth_token),
    path('posts/<int:post_id>/', include(nested_router.urls)),
    path('', include(router.urls))
]
