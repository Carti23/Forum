from rest_framework import serializers
from .models import *

# Comment Serializer
class CommentSerializer(serializers.ModelSerializer):
    comment_like = serializers.HyperlinkedIdentityField(
        view_name = 'comment-like',
        lookup_field = 'pk'
    )
    comment_detail = serializers.HyperlinkedIdentityField(
        view_name = 'comment-detail',
        lookup_field = 'pk'
    )
    class Meta:
        model = Comment
        fields = [
                    'post', 
                    'creator', 
                    'content', 
                    'liked', 
                    'likes_count',
                    'comment_like',
                    'comment_detail',
                    'file',
    ]

# Comment Create Serializer
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['post', 'creator', 'content', 'file']
        extra_kwargs = {
            'file': {'required': False}
        }

# RepeatComment Serializer
class RepeatCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepeatComment
        fields = ['comment', 'defendant', 'text', 'like', 'likes_count']

# RepeatCommentCreate Serializer
class RepeatCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RepeatComment
        fields = ['comment', 'defendant', 'text']
        

