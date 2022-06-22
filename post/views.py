from django.shortcuts import render
from rest_framework import generics, views
from .serializers import *
from .models import Post
import stripe
from rest_framework import filters
from rest_framework.permissions import *
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .permissions import PostUserWritePermission
from django.db.models import Count
from django.conf import settings



# Post List Api View
class PostListApiView(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['text', 'owner']


# Post Update Api View
class PostDetailApiView(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    permission_classes = [PostUserWritePermission, IsAuthenticated]


# Post Create Api View
class PostCreateApiView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated, ]

# Like Api View
class PostLikeApiView(views.APIView):
    # get function
    def get(self, request, pk):
        if request.user.is_authenticated:
            post = get_object_or_404(Post, pk=pk)
            if request.user in post.liked_by.all():
                post.liked_by.remove(request.user)
            else:
                post.liked_by.add(request.user)
            post.save()
            return Response({'success': True})
        else:
            return Response({'success': False})

# Top Posts API View
class TopPostsAPIView(generics.ListAPIView):

    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.annotate(
            total_likes=Count('liked_by', distinct=True)
        ).order_by('-total_likes')

# Report Post APi VIew
class ReportPostAPiView(generics.CreateAPIView):
    serializer_class = ReportPostSerializer
    queryset = Report.objects.all()

    # post function
    def post(self, request, *args, **kwargs):
        serializer = ReportPostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(report_creator = request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)





