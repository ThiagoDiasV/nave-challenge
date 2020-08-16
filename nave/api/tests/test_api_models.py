import datetime

import pytest
from django.core.validators import ValidationError

from nave.api.models import Naver


@pytest.mark.django_db
@pytest.mark.usefixtures("naver")
def test_naver_model_str_method(naver):
    assert naver.__str__() == naver.name


@pytest.mark.django_db
@pytest.mark.usefixtures("project")
def test_project_model_str_method(project):
    assert project.__str__() == project.name
