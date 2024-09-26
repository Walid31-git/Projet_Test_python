import pytest
from supermath import trigonometrie

def test_cosinus_integer():
    assert int(trigonometrie.calculer_cosinus(0)) == 1
    assert int(trigonometrie.calculer_cosinus(90)) == 0
    assert round(trigonometrie.calculer_cosinus(180)) == -1
    assert int(trigonometrie.calculer_cosinus(360)) == 1

def test_cosinus_float():
    assert pytest.approx(trigonometrie.calculer_cosinus(0.5)) == 0.87758256189
    assert pytest.approx(trigonometrie.calculer_cosinus(1.5)) == 0.07073720167
    assert pytest.approx(trigonometrie.calculer_cosinus(3.14159)) == -1

def test_sinus_integer():
    assert trigonometrie.calculer_sinus(0) == 0
    assert trigonometrie.calculer_sinus(90) == 1
    assert trigonometrie.calculer_sinus(180) == 0
    assert trigonometrie.calculer_sinus(360) == 0

def test_sinus_float():
    assert pytest.approx(trigonometrie.calculer_sinus(0.5)) == 0.4794255386
    assert pytest.approx(trigonometrie.calculer_sinus(1.5)) == 0.9974949866
    assert pytest.approx(trigonometrie.calculer_sinus(3.14159)) == 0

def test_cosinus_negative():
    assert pytest.approx(trigonometrie.calculer_cosinus(-0.5)) == 0.87758256189
    assert pytest.approx(trigonometrie.calculer_cosinus(-1.5)) == 0.07073720167

def test_sinus_negative():
    assert pytest.approx(trigonometrie.calculer_sinus(-0.5)) == -0.4794255386
    assert pytest.approx(trigonometrie.calculer_sinus(-1.5)) == -0.9974949866
