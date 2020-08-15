from django.urls import path
from . import views

# from rest_framework.routers import DefaultRouter


# router = DefaultRouter()
# router.register("navers", views.NaverViewSet, basename="navers")
# router.register("projects", views.ProjectViewSet, basename="projects")


app_name = "api"
urlpatterns = [
    path("api/signup/", views.CreateUserView.as_view(), name="create_user_view"),
    path("api/navers/", views.ListCreateNaverView.as_view(), name="create_naver_view"),
    path(
        "api/navers/<int:pk>/",
        views.RetrieveUpdateDestroyNaverView.as_view(),
        name="create_naver_view",
    ),
    path(
        "api/projects/create/",
        views.CreateProjectView.as_view(),
        name="create_project_view",
    ),
    # path(
    #     "api/",
    #     include(router.urls),
    # )
]
