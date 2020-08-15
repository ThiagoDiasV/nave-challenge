from datetime import datetime

import pytest
from django.contrib.auth import get_user_model

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
        birthdate=datetime(2012, 6, 6),
        admission_date=datetime(2016, 6, 6),
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
