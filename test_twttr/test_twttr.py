from twttr import shorten

def main():
    test_caps()
    test_digits()
    test_punctuation()


def test_caps():
    assert shorten("character") == "chrctr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("twIttEr") == "twttr"

def test_digits():
    assert shorten("12345") == "12345"

def test_punctuation():
    assert shorten("!@#%<>,.") == "!@#%<>,."



if __name__ == "__main__":
    main()
