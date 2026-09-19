import pytest
from fuel import convert, gauge

def test_covert():
    assert convert("2/3") == 67
    assert convert("2/4") == 50
    assert convert("1/4") == 25
    assert convert("0/1") == 0
    assert convert("1/1") == 100

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(50) == "50%"
    assert gauge(0) == "E"
    assert gauge(1) == "E"

def test_convert_error():
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("-1/2")
