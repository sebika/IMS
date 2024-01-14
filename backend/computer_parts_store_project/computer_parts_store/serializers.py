from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


CustomUser = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer class to serialize registration requests and create a new user.
    """
    class Meta:
        model = CustomUser
        fields = ("id", "email", "password", "first_name", "last_name", "date_joined")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_staff'] = user.is_staff

        return token
