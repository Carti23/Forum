from rest_framework import serializers
from .models import Profile
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator

# Profile Serializer
class ProfileSerializer(serializers.ModelSerializer):
    """add extra fields(update_profile link)"""
    update_profile = serializers.HyperlinkedIdentityField(
        view_name='update-profile',
        lookup_field='pk')
    add_friend = serializers.HyperlinkedIdentityField(
        view_name='sent-friend-request',
        lookup_field='pk'
    )

    class Meta:
        model = Profile
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'instagram', 'twitter', 'facebook', 'update_profile', 'friend', 'add_friend')
        extra_kwargs = {
            'email': {'required': False},
            'instagram': {'required': False},
            'twitter': {'required': False},
            'facebook': {'required': False}
        }


# Profile Update Serializer
class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = (
            'username', 'email', 'first_name',
            'last_name', 'instagram', 'twitter', 'facebook')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
            'username': {'required': False},
            'email': {'required': False},
            'instagram': {'required': False},
            'twitter': {'required': False},
            'facebook': {'required': False}
        }

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    """add extra fields"""
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=Profile.objects.all())])

    password1 = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Profile
        fields = (
            'username', 'password1', 'password2', 'email', 'first_name',
            'last_name')

        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False},
        }

    def validate(self, attrs):
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password1': "password field dont match !"})

        return attrs

    def create(self, validated_data):
        user = Profile.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        user.set_password(validated_data['password1'])
        user.save()
        return user

# Change Password Serializer
class ChangePasswordSerializer(serializers.Serializer):
    model = Profile

    """
    Serializer for password change endpoint.
    """
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

