from twttr import shorten
import pytest

def test_lowercase():
    assert shorten("miazga") == "mzg"
    assert shorten("krk") == "krk"

def test_uppercase():
    assert shorten("MIAZGA") == "MZG"
    assert shorten("KRK") == "KRK"

def test_combi():
    assert shorten("KaAcCkAa") == "KcCk"
    assert shorten("MrKKk") == "MrKKk"

def test_punc():
    assert shorten("#&\€|") == "#&\€|"
        assert shorten("!)(/)") == "!)(/)"

def test_numbers():
    assert shorten("145HOLLYWOOD45") == "145HLLYWD45"
    assert shorten("123456") == "123456"

def test_empty():
    with pytest.raises(TypeError):
        shorten()
