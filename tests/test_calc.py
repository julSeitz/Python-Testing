import pytest
from calculator.calc import add
from calculator.calc import sub

def test_add():
    assert add(6, 8) == 14
    assert add(-6, -5) == -11
    assert add(-3, 7) == 4
    assert add(0, 3) == 3
    assert add(6, -3) == 3
    assert add(9, 0) == 9

def test_sub():
    assert sub(6, 3) == 3
    assert sub(5, 7) == -2
    assert sub(-2, -5) == 3
    assert sub(-6, -4) == -2
    assert sub(-2, 8) == -10
    assert sub(-4, 3) == -7
    assert sub(4, -7) == 11
    assert sub(8, -5) == 13
    assert sub(1, 0) == 1
    assert sub(0, 5) == -5