from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    #assert hello("David") == "hello, David"
    for name in ["David", "Mike", "John"]:
        assert hello(name) == f"hello, {name}"

# pytest test
# python treates that folder as a package so we can test the whole folder
