from unittest.mock import patch
import pytest
import app

@pytest.mark.parametrize(
    "test_time, expected",
    [
        ("07:14", "Quarter past seven"),
        ("00:02", "Twelve o'clock"),
        ("18:36", "Twenty five to seven"),
        ("21:49", "Ten to ten"),
    ],
)
def test_no_user_input_calls_dependencies(test_time: str, expected: str):
    with patch('app.set_current_time', return_value=test_time):
        actual = app.no_user_input()
        assert actual == expected


@pytest.mark.parametrize(
    "test_time, expected",
    [
        ("07:10", "Ten past seven"),
        ("00:00", "Twelve o'clock"),
        ("18:30", "Half past six"),
        ("21:50", "Ten to ten"),
    ],
)
def test_with_user_input_correct_format(test_time: str, expected: str):
    actual = app.with_user_input(test_time)
    assert actual == expected


@pytest.mark.parametrize("test_time", ["07:1", "0:00", "xndj", "[15:30", "23:56[", "24:00"])
def test_with_user_input_wrong_format(test_time: str):
    actual = app.with_user_input(test_time)
    assert actual == 'Incorrect time format - use HH:MM, 24h format with 00:00 as midnight'
