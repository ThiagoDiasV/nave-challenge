from datetime import date

import pytest
from django.shortcuts import reverse


@pytest.mark.django_db
def test_create_new_user(client):
    url = reverse("api:create_user_view")

    data = {"email": "teste@teste.com", "password": "weakpassword"}
    response = client.post(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "naver")
def test_get_list_of_navers(api_client, naver):
    url = reverse("api:list_create_naver")
    response = api_client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client")
def test_post_new_naver(api_client):
    url = reverse("api:list_create_naver")
    data = {
        "name": "Naver",
        "birthdate": date(2000, 1, 1),
        "admission_date": date(2016, 1, 1),
        "job_role": "Dev",
    }
    response = api_client.post(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client")
def test_post_create_an_existing_naver(api_client):
    url = reverse("api:list_create_naver")
    data = {
        "name": "Naver",
        "birthdate": date(2000, 1, 1),
        "admission_date": date(2015, 1, 1),
        "job_role": "Dev",
    }
    api_client.post(url, data)
    second_response = api_client.post(url, data)
    assert second_response.status_code == 400
    assert second_response.json()["message"] == "This user already exists"


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client")
def test_post_create_naver_with_invalid_data(api_client):
    url = reverse("api:list_create_naver")
    data = {
        "name": "Naver",
        "birthdate": "wrong value",
        "admission_date": "wrong value 2",
        "job_role": date(2015, 1, 1),
    }
    response = api_client.post(url, data)
    assert response.status_code == 400
    assert "Date has wrong format" in response.json()["birthdate"][0]


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "naver")
def test_get_naver_detail_view(api_client, naver, project):
    url = reverse("api:retrieve_update_destroy_naver", kwargs={"pk": naver.id})
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.json()["projects"][0]["name"] == "Project"
    assert response.json()["projects"][0]["navers"][0] == naver.id


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "naver")
def test_put_naver(api_client, naver):
    url = reverse("api:retrieve_update_destroy_naver", kwargs={"pk": naver.id})
    data = {"name": "New name", "birthdate": date(2000, 1, 1), "job_role": "Dev"}
    response = api_client.put(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "naver")
def test_delete_naver(api_client, naver):
    url = reverse("api:retrieve_update_destroy_naver", kwargs={"pk": naver.id})
    response = api_client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "second_naver")
def test_user_edit_other_naver_data(api_client, second_naver):
    url = reverse("api:retrieve_update_destroy_naver", kwargs={"pk": second_naver.id})
    data = {"name": "New name", "birthdate": date(2000, 1, 1), "job_role": "Dev"}
    response = api_client.put(url, data)
    assert response.status_code == 403
    assert (
        "You do not have permission to perform this action" in response.json()["detail"]
    )


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "second_naver")
def test_user_delete_other_naver_data(api_client, second_naver):
    url = reverse("api:retrieve_update_destroy_naver", kwargs={"pk": second_naver.id})
    response = api_client.delete(url)
    assert response.status_code == 403
    assert (
        "You do not have permission to perform this action" in response.json()["detail"]
    )


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "project", "project_without_navers")
def test_get_list_of_projects(api_client, project, project_without_navers):
    url = reverse("api:list_create_project")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.json()) == 2


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "project", "project_without_navers")
def test_get_naver_specific_list_of_projects(
    api_client, project, project_without_navers
):
    url = reverse("api:list_create_project") + "?name=Project"
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert "Project" == response.json()[0]["name"]


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "naver")
def test_naver_creating_new_project(api_client, naver):
    url = reverse("api:list_create_project")
    data = {"name": "New project", "naver": naver}
    response = api_client.post(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "project")
def test_put_existing_project(api_client, project):
    url = reverse("api:retrieve_update_destroy_project", kwargs={"pk": project.id})
    data = {
        "name": "New name",
    }
    response = api_client.put(url, data)
    assert response.status_code == 200


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "project_without_navers")
def test_put_existing_project_without_ownership(api_client, project_without_navers):
    url = reverse(
        "api:retrieve_update_destroy_project", kwargs={"pk": project_without_navers.id}
    )
    data = {"name": "impossible name"}
    response = api_client.put(url, data)
    assert response.status_code == 403
    assert (
        "You do not have permission to perform this action" in response.json()["detail"]
    )


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "project")
def test_delete_existing_project(api_client, project):
    url = reverse("api:retrieve_update_destroy_project", kwargs={"pk": project.id})
    response = api_client.delete(url)
    assert response.status_code == 204


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "project_without_navers")
def test_delete_existing_project_without_ownership(api_client, project_without_navers):
    url = reverse(
        "api:retrieve_update_destroy_project", kwargs={"pk": project_without_navers.id}
    )
    response = api_client.delete(url)
    assert response.status_code == 403
    assert (
        "You do not have permission to perform this action" in response.json()["detail"]
    )


@pytest.mark.django_db
@pytest.mark.usefixtures("api_client", "project")
def test_get_project_detail_view(api_client, project):
    url = reverse("api:retrieve_update_destroy_project", kwargs={"pk": project.id})
    response = api_client.get(url)
    assert response.status_code == 200
