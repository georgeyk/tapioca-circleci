import pytest

from tapioca_circleci.tapioca_circleci import CircleCIClientAdapter


@pytest.fixture
def adapter():
    return CircleCIClientAdapter()


def test_get_request_kwargs_defaults(adapter):
    params = adapter.get_request_kwargs({})
    assert 'auth' in params
    assert 'timeout' in params
    assert params['timeout'] == 5
    assert 'headers' in params
    assert 'Content-Type' in params['headers']
    assert 'json' in params['headers']['Content-Type']


def test_get_request_kwargs_timeout(adapter):
    params = adapter.get_request_kwargs({'timeout': 10})
    assert params['timeout'] == 10

    params = adapter.get_request_kwargs({}, timeout=10)
    assert params['timeout'] == 10

    params = adapter.get_request_kwargs({'timeout': 10}, timeout=15)
    assert params['timeout'] == 10


def test_fill_resource_template_url(adapter):
    template = '{user_id}-{vcs_type}'
    result = adapter.fill_resource_template_url(template, {})
    assert result == 'me-github'

    result = adapter.fill_resource_template_url(template, {'user_id': 'other'})
    assert result == 'other-github'

    result = adapter.fill_resource_template_url(template, {'vcs_type': 'gitlab'})
    assert result == 'me-gitlab'
