from plates import is_valid

def test_rule_one():
    assert is_valid("A1") == False
    assert is_valid("12AC") == False
    assert is_valid("AB12") == True

def test_rule_two():
    assert is_valid("AAAAAAA") == False
    assert is_valid("AAAAAA") == True
    assert is_valid("A") == False
    assert is_valid("AA") == True
    assert is_valid("") == False

def test_rule_three():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AA222A") == False
    assert is_valid("AAAAA0") == False
    assert is_valid("AAA041") == False

def test_rule_four():
    assert is_valid("ABC.12") == False
    assert is_valid("ABC 1") == False
    assert is_valid("ACAA!") == False
    assert is_valid("ABC-D") == False

