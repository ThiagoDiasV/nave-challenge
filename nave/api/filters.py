from django_filters import rest_framework as filters


class NaverFilterBackends:
    """
    Filter for Naver endpoints.
    """

    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ("name", "admission_date", "job_role")
