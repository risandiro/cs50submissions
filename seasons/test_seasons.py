from seasons import validate, convert, time_to_words
import pytest

def test_validate():
    with pytest.raises(ValueError):
        validate("4000-11-11")
        validate("1111-40-11")
        validate("1111-11-40")
        validate("xx-xx-xx")

def test_convert():
    with pytest.raises(ValueError):

def test_time_to_words():

