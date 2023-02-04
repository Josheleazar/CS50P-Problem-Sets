from working import convert
import pytest

def test_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"

def test_minutes():
    assert convert("9:30 AM to 5:40 PM") == "09:30 to 17:40"

def test_range():
    with pytest.raises(ValueError):
        convert("10:70 AM to 5:60 PM")

def test_omitt_to():
    with pytest.raises(ValueError):
        convert("9:00 am 5:00 pm")

def test_format():
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")