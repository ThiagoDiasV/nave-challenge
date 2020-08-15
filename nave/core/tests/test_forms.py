from django.contrib.auth import get_user_model
from nave.core.admin import UserCreationForm
import pytest


@pytest.mark.django_db
def test_user_creation_form_with_different_passwords():
    data = {
        "email": "teste@teste.com",
        "password1": "weakpassword",
        "password2": "differentpassword",
    }
    form = UserCreationForm(data)
    form.is_valid()
    assert "Passwords don't match" in form.errors["password2"]


@pytest.mark.django_db
def test_user_creation_form_with_correct_data():
    data = {
        "email": "teste@teste.com",
        "password1": "weakpassword",
        "password2": "weakpassword",
    }
    form = UserCreationForm(data)
    form.is_valid()
    assert bool(form.errors) is False


@pytest.mark.django_db
def test_user_creation_form_save_method():
    data = {
        "email": "teste@teste.com",
        "password1": "weakpassword",
        "password2": "weakpassword",
    }
    form = UserCreationForm(data)
    form.is_valid()
    user = form.save()
    assert type(user) == get_user_model()
