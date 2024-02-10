from seasons import validate, time_to_words
import pytest

def test_validate():
    assert validate("4000-11-11") == "SystemExit: Invalid date"
    assert validate("1111-40-11") == "SystemExit: Invalid date"
    assert validate("1111-11-40") == "SystemExit: Invalid date"
    assert validate("xx-xx-xx") == "SystemExit: Invalid date"

def test_time_to_words():
    assert time_to_words(1440) == ("One thousand, four hundred forty minutes")
