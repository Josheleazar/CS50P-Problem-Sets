from um import count

def test_word_match():
    assert count("yummy") == 0

def test_case():
    assert count("UM") == 1
    assert count("um") == 1
    assert count("Um") == 1

def test_spacing():
    assert count(" Um ") == 1