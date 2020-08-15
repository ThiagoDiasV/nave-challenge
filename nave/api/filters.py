from django_filters import rest_framework as filters


class NaverFilterBackends:
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("name", "admission_date", "job_role")
