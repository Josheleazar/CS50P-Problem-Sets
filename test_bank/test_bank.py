from bank import value

def test_vals():
    assert value("What's up?") == 100
    assert value("!@#$") == 100
    assert value("12345") == 100

def test_casing():
    assert value("HELLO") == 0
    assert value("HOW'RE YOU") == 20

def test_long_phrasing():
    assert value("Hello, My name is") == 0
    assert value("Hi, My name is") == 20
    assert value("Yo, my names is") == 100