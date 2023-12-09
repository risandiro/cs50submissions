from bank import value

def test_0():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("hElLo") == 0

def test_20():
    assert value("howdy sailor") == 20
    assert value("HOWDY SAILOR") == 20
    assert value("hOwDy_sAiLoR") == 20

def test_100():
    assert value("abrakadabra") == 100
    assert value("Chuppa Chupps") == 100
    assert value() == 100
