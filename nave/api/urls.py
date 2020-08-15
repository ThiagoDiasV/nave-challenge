from django.urls import path

from . import views

app_name = "api"
urlpatterns = [
    path("api/signup/", views.CreateUserView.as_view(), name="create_user_view"),
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
