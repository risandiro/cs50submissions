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

    with pytest.raises(ValueError):
        jar = Jar("9")

    with pytest.raises(ValueError):
        jar = Jar("")

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) ==  "🍪"
    jar.deposit(11)
    assert str(jar) ==  "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"

def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert str(jar) == "🍪🍪🍪🍪🍪"
    assert jar.size == 5

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪"
    assert jar.size == 7


def test_withdraw():
    jar = Jar()
    jar.deposit(8)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"
    assert jar.size == 8
    
    jar.withdraw(4)
    assert str(jar) == "🍪🍪🍪🍪"
    assert jar.size == 4
