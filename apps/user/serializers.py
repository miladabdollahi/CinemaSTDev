from rest_framework import serializers

from apps.user.models import User


class UserBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'username'
        )
        read_only_fields = ('first_name', 'last_name', 'username')


class UserListSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta:
        model = User
        fields = ('full_name', 'is_active',)

        read_only_fields = ('full_name', 'is_active',)


class UserRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'is_active')

        read_only_fields = (
            'first_name', 'last_name', 'email', 'username', 'is_active'
        )


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'is_active', 'password')

        extra_kwargs = {
            'password': {'write_only': True, 'required': True},
            'username': {'required': True},
        }


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'is_active', 'password')

        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'username': {'required': False},
        }
