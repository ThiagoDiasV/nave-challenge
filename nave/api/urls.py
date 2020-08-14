from django.urls import path

from .views import CreateUserView

app_name = "api"
urlpatterns = [path("api/signup/", CreateUserView.as_view(), name="create_user_view")]
