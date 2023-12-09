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

def test_gauge_rounding():
    assert gauge("1/67") == "E"
    assert gauge("1/66") == "2%"
    assert gauge("100/101") == "F"
    assert gauge("93/95") == "98%"
