from fuel import convert, gauge
import pytest

def test_ints():
    assert convert("2/5") == 40

def test_val_errors():
    with pytest.raises(ValueError):
        convert("7/5")
    with pytest.raises(ValueError):
        convert("cat/2")
    with pytest.raises(ValueError):
        convert("2/cat")

def test_zerodiv_errors():
    with pytest.raises(ZeroDivisionError):
        convert("2/0")

def test_empty():
    assert gauge(1) == "E"

def test_percentage():
    assert gauge(50) == "50%"

def test_full():
    assert gauge(99) == "F"