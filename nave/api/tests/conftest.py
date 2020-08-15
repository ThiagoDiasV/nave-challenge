from datetime import date

import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from nave.api.models import Naver, Project


@pytest.fixture
def mock_user(mocker):
    yield mocker.patch("nave.core.models.User")


@pytest.fixture
def mock_naver(mocker):
    yield mocker.patch("nave.api.models.Naver")


@pytest.fixture
def mock_request(mocker):
    yield mocker.patch("django.http.HttpResponse")


@pytest.fixture
def mock_retrieve_update_delete_naver_view(mocker):
    yield mocker.patch("nave.api.views.RetrieveUpdateDestroyNaverView")


@pytest.fixture
def mock_project(mocker):
    yield mocker.patch("nave.api.models.Project")


@pytest.fixture
def mock_retrieve_update_delete_project_view(mocker):
    yield mocker.patch("nave.api.views.RetrieveUpdateDestroyProjectView")


@pytest.fixture
@pytest.mark.django_db
def user():
    user = get_user_model().objects.create_user("teste@teste.com", "12345")
    yield user


@pytest.fixture
@pytest.mark.django_db
def naver(user):
    naver = Naver.objects.create(
        user=user,
        name="teste",
        birthdate=date(2012, 6, 6),
        admission_date=date(2016, 6, 6),
        job_role="Dev",
    )
    yield naver


@pytest.fixture
@pytest.mark.django_db
def project(naver):
    project = Project.objects.create(name="Project")
    project.navers.add(naver)
    yield project


@pytest.fixture
@pytest.mark.django_db
def project_without_navers():
    project = Project.objects.create(name="Project no navers")
    yield project


@pytest.fixture
def api_client(user):
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {refresh.access_token}")

    return client


@pytest.fixture
@pytest.mark.django_db
def second_user():
    user = get_user_model().objects.create_user("teste2@teste.com", "12345")
    yield user


@pytest.fixture
@pytest.mark.django_db
def second_naver(second_user):
    naver = Naver.objects.create(
        user=second_user, name="teste2", birthdate=date(2000, 1, 1), job_role="Dev"
    )
    yield naver
