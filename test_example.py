import pytest 
def test_dodaj():
    assert dodaj(2, 3) == 5
    

def test_odejmij():
    assert odejmij(5, 3) == 2
    

def test_mnoz():
    assert mnoz(2, 3) == 6
   

def test_dziel():
    assert dziel(6, 3) == 2
   
    with pytest.raises(ValueError):
        dziel(6, 0)

