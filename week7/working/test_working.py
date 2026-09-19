from working import convert

import pytest


def test1():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test2():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test3():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9 AM to 5:00 PM") == "09:00 to 17:00"


def test4():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test5():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("9:00 AM 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:60 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("13:00 AM to 5:00 PM")

    with pytest.raises(ValueError):
        convert("9:00 AM to 5:000 PM")
