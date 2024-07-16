# tests/test_calculator.py
from app.calculator import add

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 1) == 0
