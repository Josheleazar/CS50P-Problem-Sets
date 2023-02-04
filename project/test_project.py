from project import cap_rate, annual_rev, assets
import pytest

def test_annual_rev():
    assert annual_rev(50, 1000) == 50000

def test_cap_rate():
    assert cap_rate(50000, 5000000) == 12.0

def test_assets():
    assert assets("50", "1000") == (50, 1000)
    with pytest.raises(SystemExit):
        assets("Fifty", "1000")
    with pytest.raises(SystemExit):
        assets("50", "One Thousand")
    with pytest.raises(SystemExit):
        assets("Fifty", "One Thousand")
