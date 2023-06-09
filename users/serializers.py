from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ParseError
import re
from groups.serializers import GroupSerializer


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "pk",
            "is_coach",
        )


class PrivateUserSerializer(ModelSerializer):
    date_joined = serializers.DateTimeField(read_only=True)
    avatar = serializers.URLField(read_only=True)
    group = GroupSerializer(read_only=True)

    class Meta:
        model = User
        exclude = (
            "first_name",
            "last_name",
            "last_login",
            "password",
            "is_superuser",
            "is_staff",
            "is_active",
            "groups",
            "user_permissions",
        )

    def validate_phone_number(self, data):
        phone_regex = re.compile(r"^010\d{4}\d{4}$")
        data = data.replace("-", "")
        if not phone_regex.match(data):
            raise serializers.ValidationError("유효한 형식을 입력하세요.")
        return data
