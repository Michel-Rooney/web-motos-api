from rest_framework import serializers

from .models import Carro
from .models import UserBase


class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        exclude = ['created_at', 'updated_at']


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserBase
        fields = ['id', 'username', 'email', 'favorites', 'password']

    def create(self, validated_data):
        user = UserBase.objects.create_user(**validated_data)

        return user
