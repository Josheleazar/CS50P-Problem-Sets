from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar2 = Jar(7)
    assert jar2.capacity == 7


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2

def test_withdraw():
    jar = Jar()
    jar.deposit(6)
    jar.withdraw(2)
    assert jar.size == 4

