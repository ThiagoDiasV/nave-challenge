import pytest

from nave.api.permissions import IsNaverUserOrReadOnly, IsProjectNaverOrReadOnly


@pytest.mark.usefixtures(
    "mock_naver", "mock_request", "mock_retrieve_update_delete_naver_view",
)
def test_is_naver_user_or_read_only_permission_using_not_safe_methods(
    mock_naver, mock_request, mock_retrieve_update_delete_naver_view
):
    mock_naver.user = mock_request.user
    permission = IsNaverUserOrReadOnly()
    assert (
        permission.has_object_permission(
            mock_request, mock_retrieve_update_delete_naver_view, mock_naver
        )
        is True
    )


@pytest.mark.usefixtures(
    "mock_naver", "mock_request", "mock_retrieve_update_delete_naver_view",
)
def test_is_naver_user_or_read_only_permission_using_safe_methods(
    mock_naver, mock_request, mock_retrieve_update_delete_naver_view
):
    mock_naver.user = mock_request.user
    mock_request.method = "GET"
    permission = IsNaverUserOrReadOnly()
    assert (
        permission.has_object_permission(
            mock_request, mock_retrieve_update_delete_naver_view, mock_naver
        )
        is True
    )


@pytest.mark.usefixtures(
    "mock_project", "mock_request", "mock_retrieve_update_delete_project_view",
)
def test_is_project_naver_or_read_only_permission_using_safe_methods(
    mock_project, mock_request, mock_retrieve_update_delete_project_view
):
    mock_project.user = mock_request.user
    mock_request.method = "GET"
    permission = IsProjectNaverOrReadOnly()
    assert (
        permission.has_object_permission(
            mock_request, mock_retrieve_update_delete_project_view, mock_project
        )
        is True
    )


@pytest.mark.django_db
@pytest.mark.usefixtures(
    "mock_retrieve_update_delete_project_view", "mock_request", "project", "user"
)
def test_is_project_naver_or_read_only_permission_using_unsafe_methods(
    mock_retrieve_update_delete_project_view, mock_request, project, user
):
    permission = IsProjectNaverOrReadOnly()
    mock_request.user = user
    assert (
        permission.has_object_permission(
            mock_request, mock_retrieve_update_delete_project_view, project
        )
    ) is True


@pytest.mark.django_db
@pytest.mark.usefixtures(
    "mock_retrieve_update_delete_project_view",
    "mock_request",
    "user",
    "project_without_navers",
)
def test_is_project_naver_or_read_only_permission_using_unsafe_methods_and_raising_exception(
    mock_retrieve_update_delete_project_view, mock_request, user, project_without_navers
):
    permission = IsProjectNaverOrReadOnly()
    mock_request.user = user
    assert (
        permission.has_object_permission(
            mock_request,
            mock_retrieve_update_delete_project_view,
            project_without_navers,
        )
    ) is False
