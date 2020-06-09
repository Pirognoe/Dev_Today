#  DRF imports below:
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

#  Application imports below:
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from django.http import HttpResponse


def home_view(*args, **kwargs):
    return HttpResponse("<h1>Hello</h1>")


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        post = self.get_object()
        post.amount_of_upvotes += 1
        post.save()
        return Response({'status': 'Upvoted'})


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
