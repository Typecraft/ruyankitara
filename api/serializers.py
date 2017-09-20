from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser')
        read_only_fields = ('url', 'id', 'is_active', 'is_staff', 'is_superuser')
