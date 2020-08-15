import pytest
from django.shortcuts import reverse


@pytest.mark.django_db
def test_create_new_user(client):
    url = reverse("api:create_user_view")

    data = {"email": "teste@teste.com", "password": "weakpassword"}
    response = client.post(url, data)
    assert response.status_code == 201
