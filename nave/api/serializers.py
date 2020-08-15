from rest_framework import serializers

from .models import Naver, Project


class NaverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Naver
        exclude = ("user",)

    def get_fields(self, *args, **kwargs):
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get("request")
        if request is not None:
            if not request.parser_context.get("kwargs") and request.method == "GET":
                fields.pop("projects")
        return fields


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"


class NaverSerializerDepth1(serializers.ModelSerializer):
    class Meta:
        model = Naver
        exclude = ("user",)
        depth = 1


class ProjectSerializerDepth1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        depth = 1
