__all__ = ()
import pytest
from routes import setup_routes
from sanic import Sanic


@pytest.fixture(scope='session')
def app():
    sanic_app = Sanic('TestApp')
    setup_routes(sanic_app)
    return sanic_app


def test_create_link_success(app, mocker):
    mock_redis = mocker.MagicMock()
    mocker.patch(
        'config.AppConfig.get_redis',
        new_callable=mocker.PropertyMock,
        return_value=mock_redis,
    )

    request, response = app.test_client.post(
        '/shorten',
        json={'link': 'http://google.com'},
    )
    assert response.status == 201
    assert response.json['status'] == 'success'
    assert 'short_url' in response.json
    assert 'id' in response.json
    mock_redis.set.assert_called_once()


def test_create_link_invalid_url(app, mocker):
    mock_redis = mocker.MagicMock()

    mocker.patch(
        'config.AppConfig.get_redis',
        new_callable=mocker.PropertyMock,
        return_value=mock_redis,
    )

    request, response = app.test_client.post(
        '/shorten',
        json={'link': 'yandex.ru'},
    )
    assert response.status != 201


def test_get_link_success(app, mocker):
    mock_redis = mocker.MagicMock()
    mock_redis.get.return_value = b'http://google.com'

    mocker.patch(
        'config.AppConfig.get_redis',
        new_callable=mocker.PropertyMock,
        return_value=mock_redis,
    )

    request, response = app.test_client.get('/long/test123')

    assert response.status == 200
    assert response.json['status'] == 'success'
    assert response.json['link'] == 'http://google.com'
    mock_redis.get.assert_called_with('test123')


def test_get_link_not_found(app, mocker):
    mock_redis = mocker.MagicMock()
    mock_redis.get.return_value = None

    mocker.patch(
        'config.AppConfig.get_redis',
        new_callable=mocker.PropertyMock,
        return_value=mock_redis,
    )

    request, response = app.test_client.get('/long/missing')

    assert response.status == 404
    assert response.json['status'] == 'error'
    assert 'не найдена' in response.json['message']
