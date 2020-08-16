from django.contrib import admin
from django.views.generic import RedirectView
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from nave.api import urls as api_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(api_urls)),
    path("", RedirectView.as_view(pattern_name='schema-swagger-ui')),
]

urlpatterns += [
    path("api-auth/", include("rest_framework.urls")),
]

schema_view = get_schema_view(
    openapi.Info(
        title="nave API", default_version="v1", description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    re_path(
        r"openapi/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "openapi/swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "openapi/redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
