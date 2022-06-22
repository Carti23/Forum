from rest_framework import serializers
from .models import Post, Report

# Post Serializer
class PostSerializer(serializers.ModelSerializer):
    like_url = serializers.HyperlinkedIdentityField(
        view_name="post-like",
        lookup_field='pk'
    )
    detail_url = serializers.HyperlinkedIdentityField(
        view_name = 'post-detail',
        lookup_field = 'pk'
    )

    class Meta:
        model = Post
        fields = [
                'text',
                'owner',
                'image',
                'links',
                'files',
                'liked_by',
                'likes_count',
                'like_url',
                'detail_url',
        ]

# Post Create Serializer
class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
                    'text',
                    'owner',
                    'image',
                    'links',
                    'files'
        ]
        extra_kwargs = {
            'files': {'required': False},
            'image': {'required': False},
            'links': {'required': False},
        }

# Report Post Serializer
class ReportPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            'post',
            'report_creator',
            'text'
        ]

class PostProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'text'
        ]



