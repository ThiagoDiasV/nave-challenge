from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for custom user model.
    """

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()

        return user

    class Meta:
        model = User
        fields = ["id", "email", "password"]
