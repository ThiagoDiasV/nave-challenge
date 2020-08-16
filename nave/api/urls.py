from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from . import views

app_name = "api"
urlpatterns = [
    path("api/signup/", views.CreateUserView.as_view(), name="create_user_view"),
    path("api/login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/navers/", views.ListCreateNaverView.as_view(), name="list_create_naver"),
    path(
        "api/navers/<int:pk>/",
        views.RetrieveUpdateDestroyNaverView.as_view(),
        name="retrieve_update_destroy_naver",
    ),
    path(
        "api/projects/",
        views.ListCreateProjectView.as_view(),
        name="list_create_project",
    ),
    path(
        "api/projects/<int:pk>/",
        views.RetrieveUpdateDestroyProjectView.as_view(),
        name="retrieve_update_destroy_project",
    ),
]
