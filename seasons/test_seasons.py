from seasons import get_birthday
import datetime

def test_birthday():
    assert get_birthday("2022-01-18") == datetime.date(2022, 1, 18)