from fuel import convert, gauge
import pytest


def test_x_is_greater_than_y():
    with pytest.raises(ValueError):
        convert("4/3")

def test_x_is_not_an_integer():
    with pytest.raises(ValueError):
        convert("x/3")

def test_x_is_not_an_integer():
    with pytest.raises(ValueError):
        convert("3/x")

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")

def test_convert():
    assert convert("1/2") == 50
    assert convert("15/57") == 26
    assert convert("1/100") == 1
    assert convert("99/100") == 99
    assert convert("1/1") == 100

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
