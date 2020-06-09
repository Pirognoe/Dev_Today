from rest_framework import serializers
from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    # up_vote = serializers.SerializerMethodField('cast_up_vote', write_only=True)

    class Meta:
        model = Post
        fields = '__all__'  # All fields are checked to ensure full CRUD


class CommentSerializer(serializers.ModelSerializer):
    post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
