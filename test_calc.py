import pytest
from calc import add

def test_add():
    assert add(6, 8) == 14
    assert add(-6, -5) == -11
    assert add(-3, 7) == 4
    assert add(0, 3) == 3
    assert add(6, -3) == 3
    assert add(9, 0) == 9