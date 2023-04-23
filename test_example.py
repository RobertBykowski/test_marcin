import pytest 
def test_dodaj():
    assert dodaj(2, 3) == 5
    assert dodaj(-2, 2) == 0
    assert dodaj(0, 0) == 0

def test_odejmij():
    assert odejmij(5, 3) == 2
    assert odejmij(-2, 2) == -4
    assert odejmij(0, 0) == 0

def test_mnoz():
    assert mnoz(2, 3) == 6
    assert mnoz(-2, 2) == -4
    assert mnoz(0, 0) == 0

def test_dziel():
    assert dziel(6, 3) == 2
    assert dziel(-4, 2) == -2
    assert dziel(0, 5) == 0
    with pytest.raises(ValueError):
        dziel(6, 0)

