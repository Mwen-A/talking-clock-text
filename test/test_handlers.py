import pytest
from datetime import datetime
import handlers

def test_current_time_returns_time():
    expected = handlers.set_current_time()
    assert expected == datetime.now().strftime("%H:%M")


@pytest.mark.parametrize(
    "test_time, expected",
    [("15:32", "15:30"), ("11:48", "11:50"), ("01:16", "01:15"), ("20:00", "20:00")],
)
def test_time_reformat_case(test_time, expected):
    actual = handlers.reformat_time(test_time)
    assert actual == expected


@pytest.mark.parametrize(
    "test_time, expected",
    [
        ("05:10", "ten past five"),
        ("00:00", "twelve o'clock"),
        ("13:30", "half past one"),
        ("23:50", "ten to twelve"),
    ],
)
def test_sentence_construction(test_time, expected):
    actual = handlers.sentence_construction(test_time)
    assert actual == expected
