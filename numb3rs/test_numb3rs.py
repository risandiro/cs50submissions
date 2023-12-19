from numb3rs import validate

def test_validate_range():
    assert validate("255.255.0.255") == True
    assert validate("256.0.0.254") == False
    assert validate("-1.5.85.47") == False
    assert validate("1.2.3.4") == True

def test_validate_input():
    assert validate(".1.2.3.4)
