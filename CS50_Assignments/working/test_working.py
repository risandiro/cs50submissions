from working import convert
import pytest


def test_normal():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_abnormal():
    with pytest.raises(ValueError):
        convert("13 AM to 15 PM")



def test_invalid():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
