import pytest
from Code import odd_2

def test_odd_square():
    assert odd_2.odd_squre([1,2,3,4,5,6,7,8,9]) == [1, 9, 25, 49, 81]