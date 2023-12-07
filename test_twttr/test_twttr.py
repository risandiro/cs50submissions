from twttr import shorten


def test_lowercase():
    assert shorten("miazga") == "Output: mzg"
    assert shorten("krk") == "Output: krk"

def test_uppercase():
    assert shorten("MIAZGA") == "Output: MZG"
    assert shorten("KRK") == "Output: KRK"

def test_integer():
    assert shorten(int(5)) == "Output: 5"
