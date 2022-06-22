from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from post.serializers import PostSerializer
from user.models import Profile
from user.serializers import ProfileSerializer

# Search APi View
class SearchApiView(APIView):
    http_method_names = ['get']

    def get(self, request, format=None, **kwargs):
        search_term = request.GET.get('q', '')

        serializer_context = {
            'request': request
        }

        posts = PostSerializer(
            Post.objects.filter(text__icontains=search_term),
            many=True,
            context=serializer_context
        )
        users = ProfileSerializer(
            Profile.objects.filter(username__icontains=search_term),
            many=True,
            context=serializer_context
        )

        data = {
            'posts': posts.data,
            'users': users.data,
        }

        return Response(data=data)