import logging
from .serializers import *
from .models import Profile
from rest_framework import generics, views
from rest_framework import filters
from rest_framework.permissions import *
from rest_framework.response import Response
from .permissions import IsUpdateProfile
from rest_framework import status
from post.models import Post
from post.serializers import PostProfileSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from friendship.models import Friend, Follow, Block, FriendshipRequest

logger = logging.getLogger('user')

# Profile List Api View
class ProfileListApiView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'first_name', 'last_name', 'username']


# Profile Update Api View
class ProfileDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProfileUpdateSerializer
    queryset = Profile.objects.all()
    permission_classes = [IsUpdateProfile, IsAuthenticated]

# Register Api View
class RegisterView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    permission_classes = (AllowAny,)
    logger.info('hello!')
    serializer_class = RegisterSerializer

# Post User APi View
class PostUserApiView(generics.ListAPIView):
    queryset = Post.objects.all()

    def get(self, request):
        user = request.user
        post = Post.objects.filter(owner=user)
        serializer = PostProfileSerializer(post, many=True)
        return Response(serializer.data)

# MyToken Serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

# Login Api View
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = Profile
    # permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
            }

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Sent Friend Request To The User
class SentFriendRequestView(views.APIView):
    def post(self, request, *args, **kwargs):
        other_user = Profile.objects.get(pk=request.data['other_user'])
        Friend.objects.add_friend(
            request.user,
            request.user,
            pk=other_user,
            message = "Hi! i would like to add you")
        return Response({"status": "Request sent"}, status=201)


# Accept Friend Request
class AddFriendView(views.APIView):
     def post(self, request, *args, **kwargs):
         friend_request = FriendshipRequest.objects.get(to_user=request.user)
         friend_request.accept()
         return Response({'status': "Sent"}, status=201)

# Add Follower Api View
class AddFollowerView(views.APIView):
    def post(self, request, *args, **kwargs):
        other_user = Profile.objects.get(pk=request.data['other_user'])
        Follow.objects.add_follower(
            request.user,
            other_user)
        return Response({'status': "Accepted"}, status=201)


# Remove Friends Api View
class RemoveFriendsApiView(views.APIView):
    def post(self, request, *args, **kwargs):
        other_user = Profile.objects.get(pk=request.data['other_user'])
        Friend.objects.remove_friend(
            request.user,
            other_user)
        return Response({'status': "Removed"}, status=201)

# Add to the Block Api View
class AddToBlockApiView(views.APIView):
    def post(self, request, *args, **kwargs):
        other_user = Profile.objects.get(pk=request.data['other_user'])
        Block.objects.add_block(
            request.user,
            other_user)
        return Response({'status': "Added to the block"}, status=201)

# Delete from block
class DeleteFromBlockApiView(views.APIView):
    def post(self, request, *args, **kwargs):
        other_user = Profile.objects.get(pk=request.data['other_user'])
        Block.objects.remove_block(
            request.user,
            other_user)
        return Response({'status': "Added to the block"}, status=201)
