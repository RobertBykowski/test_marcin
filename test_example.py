from kalkulator import dodaj, odejmij, pomnoz, podziel
import pytest

def test_dodaj():
    assert dodaj(2, 3) == 5

def test_odejmij():
    assert odejmij(5, 2) == 3

def test_pomnoz():
    assert pomnoz(4, 6) == 24

def test_podziel():
    assert podziel(10, 2) == 5
    with pytest.raises(ZeroDivisionError):
        podziel(5, 0)

    



