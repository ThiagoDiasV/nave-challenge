from .models import Naver
from rest_framework import serializers


class NaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naver
        exclude = ("user",)
        # depth = 1
        extra_kwargs = {"projects": {"required": True}}
