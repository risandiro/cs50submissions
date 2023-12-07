from twttr import shorten

def test_string():
    assert shorten("miazga") == "mzg"

def test_integer():
    assert shorten(int(1)) == int(1)
