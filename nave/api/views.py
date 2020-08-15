from django.contrib.auth import get_user_model
from rest_framework import permissions, authentication, status
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response
from nave.naver.models import Naver
from nave.naver.serializers import NaverSerializer
from nave.project.models import Project
from nave.project.serializers import ProjectSerializer
from .permissions import IsOwnerOrReadOnly

from nave.core.serializers import UserSerializer

User = get_user_model()


class CreateUserView(CreateAPIView):
    """
    View to create new users.
    """

    model = get_user_model()
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer


# class NaverViewSet(ModelViewSet):
#     """
#     Naver ModelViewSet.

#     Requires token authentication.
#     """

#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Naver.objects.all()
#     serializer_class = NaverSerializer


# class ProjectViewSet(ModelViewSet):
#     """
#     Project ModelViewSet.

#     Requires token authentication.
#     """

#     authentication_classes = [authentication.SessionAuthentication]
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer


class ListCreateNaverView(ListCreateAPIView):
    """
    View to create new navers.

    Requires token authentication.
    """

    authentication_classes = [authentication.SessionAuthentication]
    # authentication_classes = [authentication.TokenAuthentication]
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
    authentication_classes = [authentication.SessionAuthentication]
    # authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    model = Naver
    serializer_class = NaverSerializer
    queryset = Naver.objects.all()


class CreateProjectView(CreateAPIView):
    """
    View to create new projects.

    Requires token authentication.
    """

    # authentication_classes = [authentication.TokenAuthentication]
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    model = Project
    serializer_class = ProjectSerializer


# class ListNavers(APIView):
#     """
#     View to list all navers in the system.

#     Requires token authentication.
#     """

#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         """
#         Return a list of all navers.
#         """
#         navers = [naver for naver in Naver.objects.all()]
#         return Response(navers)


# class ListNavers(APIView):
#     """
#     View to list all navers in the system.

#     Requires token authentication.
#     """

#     authentication_classes = [authentication.TokenAuthentication]
#     permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         """
#         Return a list of all navers.
#         """
#         navers = [naver for naver in Naver.objects.all()]
#         return Response(navers)
