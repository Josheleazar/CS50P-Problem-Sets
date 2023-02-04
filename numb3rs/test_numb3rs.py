from numb3rs import validate

def test_invalid_format():
    assert validate("2001:0db8:85a3:0000:0000:8a2e:0370:7334") == False

def test_first_byte():
    assert validate("255.256.500.255") == False
