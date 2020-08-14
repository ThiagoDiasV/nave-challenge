from django.shortcuts import reverse
from django.contrib.auth import get_user_model
import pytest


@pytest.mark.django_db
def test_create_new_user_without_email_info():
    with pytest.raises(ValueError):
        get_user_model().objects.create_user(
            email="",
            password="blablabla"
        )


@pytest.mark.django_db
def test_create_new_user_successfully():
    get_user_model().objects.create_user(
        email="nave@nave.com",
        password="blablabla"
    )

    user = get_user_model().objects.get(email='nave@nave.com')
    assert type(user) == get_user_model()


@pytest.mark.django_db
def test_create_new_superuser_successfully():
    get_user_model().objects.create_superuser(
        email="supernave@nave.com",
        password="blablabla"
    )

    superuser = get_user_model().objects.get(email='supernave@nave.com')
    assert superuser.is_staff is True


@pytest.mark.django_db
def test_user_methods():
    get_user_model().objects.create_user(
        email="nave@nave.com",
        password="blablabla"
    )

    user = get_user_model().objects.get(email='nave@nave.com')
    user.clean()
    user.email_user('subject', 'message')
    assert user.get_full_name() == user.email
    assert user.get_short_name() == user.email
