from plates import is_valid

def test_alphabet():
    assert is_valid("22CS") == False
    assert is_valid("CS50") == True
    assert is_valid("22") == False

def test_length():
    assert is_valid("AAAAAA") == True
    assert is_valid("CS") == True
    assert is_valid("C") == False
    assert is_valid("AAAAAAAA") == False

def test_number_place():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("AAA22A") == False

def test_alphanumeric():
    assert is_valid("CS@#") == False
