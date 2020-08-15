from django.contrib.auth import get_user_model
from rest_framework import permissions, status
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from nave.core.serializers import UserSerializer

from .filters import NaverFilterBackends
from .models import Naver, Project
from .permissions import IsNaverUserOrReadOnly, IsProjectNaverOrReadOnly
from .serializers import (
    NaverSerializer,
    NaverSerializerDepth1,
    ProjectSerializer,
    ProjectSerializerDepth1,
)

User = get_user_model()


class CreateUserView(CreateAPIView):
    """
    View to create new users.
    """

    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


class ListCreateNaverView(ListCreateAPIView, NaverFilterBackends):
    """
    View to create new navers.

    Requires jwt authentication.
    """

    permission_classes = [permissions.IsAuthenticated]
    model = Naver
    serializer_class = NaverSerializer
    queryset = Naver.objects.all()

    def post(self, request):
        naver_serializer = NaverSerializer(data=request.data)
        if naver_serializer.is_valid():
            try:
                Naver.objects.get(user=self.request.user)
            except Naver.DoesNotExist:
                naver_serializer.save(user=self.request.user)
                return Response(naver_serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(
                    data={"message": "This user already exists"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return Response(
            data=naver_serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )


class RetrieveUpdateDestroyNaverView(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or destroy a naver.

    Requires jwt authentication.
    """

    permission_classes = [permissions.IsAuthenticated, IsNaverUserOrReadOnly]
    model = Naver
    queryset = Naver.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return NaverSerializerDepth1
        return NaverSerializer


class ListCreateProjectView(ListCreateAPIView):
    """
    View to list or create new projects.

    Requires jwt authentication.
    """

    permission_classes = [permissions.IsAuthenticated]
    model = Project
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class RetrieveUpdateDestroyProjectView(RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update or destroy a project.

    Requires jwt authentication.
    """

    permission_classes = [permissions.IsAuthenticated, IsProjectNaverOrReadOnly]
    model = Project
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return ProjectSerializerDepth1
        return ProjectSerializer
