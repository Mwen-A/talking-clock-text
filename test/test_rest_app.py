from flask import Flask, request
import rest_app
from unittest.mock import patch

app = Flask(__name__)

def test_request_times_get():
    with app.test_request_context('/', method='GET'):
            with patch('app.set_current_time', return_value='10:05'):
                expected = rest_app.request_times()
                assert request.path == '/'
                assert expected == '{"payload_message": "Five past ten"}'


def test_request_times_post():
    with app.test_request_context('/', method='POST', data='10:05'):
        expected = rest_app.request_times()
        assert request.path == '/'
        assert expected == '{"payload_message": "Five past ten"}'


def test_request_times_post_invalid_format():
    with app.test_request_context('/', method='POST', data='XX'):
        expected = rest_app.request_times()
        assert request.path == '/'
        assert expected == '{"payload_message": "Incorrect time format - use HH:MM, 24h format with 00:00 as midnight"}'
