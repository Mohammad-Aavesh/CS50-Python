from seasons import convert
import pytest


def test_valid_date():

    assert convert("2000-01-01") == convert("2000-01-01")

    assert convert("2026-06-24") == convert("2026-06-24")


def test_valid_error():

    with pytest.raises(ValueError):
        convert("Februry 6th, 1998")

    with pytest.raises(ValueError):
        convert("1990-50-50")
