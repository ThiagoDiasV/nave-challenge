from nave.api.serializers import NaverSerializer
import pytest


@pytest.mark.usefixtures(
    'mock_request'
)
def test_naver_serializer_get_fields_method(mock_request):
    serializer = NaverSerializer()
    serializer.context['request'] = mock_request
    fields = serializer.get_fields()
    assert bool(fields['projects']) is True


@pytest.mark.usefixtures(
    'mock_request'
)
def test_naver_serializer_get_fields_method_pop_projects(mock_request):
    serializer = NaverSerializer()
    mock_request.method = 'GET'
    mock_request.parser_context.get.return_value = False
    serializer.context['request'] = mock_request
    fields = serializer.get_fields()
    with pytest.raises(KeyError):
        fields['projects']
