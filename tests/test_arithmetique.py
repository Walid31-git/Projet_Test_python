import pytest 
from supermath import arithmetique

def test_integer():
    assert arithmetique.additionner(2,2) == 4
    assert arithmetique.additionner(-2, 3) == 1
    assert arithmetique.additionner(-2 ,-2) == -4
    
def test_addition_float():
    assert arithmetique.additionner(2.2, 2) == 4.2
    assert arithmetique.additionner(-2.2, 3) == 0.8
    assert arithmetique.additionner(-2.2,-2) == 4.2
    
def test_soustraction_integer():
    assert arithmetique.soustraire(2,2) == 0
    assert arithmetique.soustraire(-2, 3) == -5
    assert arithmetique.soustraire(-2 ,-2) == 0
    
def test_soustraction_float():
    assert arithmetique.soustraire(2.2, 2) == 0.2
    assert arithmetique.soustraire(-2.2, 3) == -5.2
    assert arithmetique.soustraire(-2.2,-2) == -0.2
    
def test_multiplication_integer():
    assert arithmetique.multiplier(2, 2) == 4
    assert arithmetique.multiplier(-2, 3) == -6
    assert arithmetique.multiplier(-2, -2) == 4

def test_multiplication_float():
    assert arithmetique.multiplier(2.2, 2) == 4.4
    assert arithmetique.multiplier(-2.2, 3) == -6.6
    assert arithmetique.multiplier(-2.2, -2) == 4.4

def test_division_integer():
    assert arithmetique.diviser(2, 2) == 1
    assert arithmetique.diviser(-2, 3) == -2 / 3
    assert arithmetique.diviser(-2, -2) == 1

def test_division_float():
    assert arithmetique.diviser(2.2, 2) == 1.1
    assert arithmetique.diviser(-2.2, 3) == -2.2 / 3
    assert arithmetique.diviser(-2.2, -2) == 1.1