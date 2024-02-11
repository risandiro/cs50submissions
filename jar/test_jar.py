import pytest
from jar import Jar

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar = Jar(7)
    assert jar.capacity == 7
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar = Jar(-5)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) ==  "🍪"
    jar.deposit(11)
    assert str(jar) ==  "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    ...

def test_withdraw():
    ...
