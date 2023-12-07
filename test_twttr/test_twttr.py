from twttr import shorten

def main()
    test_lowercase()
    test_uppercase()
    test_integer()

def test_lowercase():
    assert shorten("miazga") == "Output: mzg"
    assert shorten("krk") == "Output: krk"

def test_uppercase():
    assert shorten("MIAZGA") == "Output: MZG"
    assert shorten("KRK") == "Output: KRK"

def test_integer():
    assert shorten(int(5)) == "Output: 5"

if __name__ == "__main__":
    main()
