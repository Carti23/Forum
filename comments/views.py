from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics, views
from rest_framework.permissions import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .permissions import CommentUserWritePermission
from django.db.models import Count

# Comment List Api View
class CommentListApiView(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated, ]

# Comment Create Api View
class CommentCreateApiView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated, ]

    # post function
    def post(self, request, *args, **kwargs):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(creator = request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)

# Comment Detail Api View
class CommentDetailDestroyApiView(generics.RetrieveUpdateDestroyAPIView, CommentUserWritePermission):
    queryset = Comment.objects.all()
    lookup_field = "pk"
    serializer_class = CommentCreateSerializer
    permission_classes = [CommentUserWritePermission, IsAuthenticated]

# Like Api View
class CommentLikeApiView(views.APIView):
    # get function
    def get(self, request, pk):
        if request.user.is_authenticated:
            post = get_object_or_404(Comment, pk=pk)
            if request.user in post.liked.all():
                post.liked.remove(request.user)
            else:
                post.liked.add(request.user)
            post.save()
            return Response({'success': True})
        else:
            return Response({'success': False})

# RepeatComment List Api View
class RepeatCommentListApiView(generics.ListAPIView):
    queryset = RepeatComment.objects.all()
    serializer_class = RepeatCommentSerializer
    permission_classes = [IsAuthenticated, ]

# RepeatComment Create Api View
class RepeatCommentCreateApiView(generics.CreateAPIView):
    queryset = RepeatComment.objects.all()
    serializer_class = RepeatCommentCreateSerializer
    permission_classes = [IsAuthenticated, ]

    # post function
    def post(self, request, *args, **kwargs):
        serializer = RepeatCommentCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(defendant = request.user)
            return Response(serializer.data, status=200)
        else:
            return Response({"errors": serializer.errors}, status=400)

# RepeatCommentDetail Api View
class RepeatCommentDetailDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RepeatComment.objects.all()
    lookup_field = "pk"
    serializer_class = RepeatCommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# Top Comments Api View
class TopCommentsAPIView(generics.ListAPIView):

    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.annotate(
            total_likes=Count('liked', distinct=True)
        ).order_by('-total_likes')




