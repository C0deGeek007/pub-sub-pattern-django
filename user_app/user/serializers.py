from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
# from .userSerializer import UserSerializers


class permissionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Permission
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):

    user_permissions = permissionSerializer(many=True)

    class Meta:
        model=User
        fields='__all__'
