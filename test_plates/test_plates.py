import plates

def test_rule_one():
    assert is_valid("AA") == True
    assert is_valid("A1") == False
    assert is_valid("AA1") == True

def test_rule_two():
    assert is_valid(")

