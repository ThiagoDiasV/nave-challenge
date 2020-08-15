from .models import Project
from rest_framework import serializers
from nave.naver.serializers import NaverSerializer

# from nave.naver.models import Naver


class ProjectSerializer(serializers.ModelSerializer):
    navers = NaverSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "navers",
        )
        extra_kwargs = {"navers": {"required": True}}
        # depth = 1
