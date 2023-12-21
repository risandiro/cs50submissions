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
        convert("9:60 AM to 5:60 PM")
        convert("12:01 AM to 12:00 PM")
        convert("12:00 AM to 12:01 PM")
        convert("13:00 AM to 12:00 PM")
        convert("12:00 AM to 13:00 PM")


def test_invalid():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("09:00 AM - 17:00 PM")
        convert("9 AM to  11 AM")
        convert("9 AM  to 11 AM")
        convert("9 AM to  11 AM")
        convert("9 AM too 11 AM")
        convert("9 AM ui 11 AM")
        convert("9 AM TO 11 AM")
        convert("9 AM 11 AM")
        convert("9:20 PM bo 7 AM")
        convert("9 AM11 AM")
        convert("9 PM mu 11:52 AM")
        convert("9 SM to 11:52 AM")
        convert("9 AM to 11:52 SM")
        convert("11:47 PM .. 1 PM")
        convert("10:01 AM10:02 PM")
        convert("4 AM tu 14:11 AM")
        convert("9 to 11:52 AM")
        convert("11:52 PM to 11:52")
        convert("9 AM")
        convert("9 to 5")
        convert("9 PM to")
        convert("9 PM to ")
        convert("to")
        convert(" to ")
        convert("")
        convert()





