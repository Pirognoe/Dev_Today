from rest_framework.routers import SimpleRouter
from django.conf.urls import url, include
from .views import PostViewSet, CommentViewSet

router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns = [
    url(r'^', include(router.urls)),
]
