import pytest
from Code import vowels

def test_vow():
    assert vowels.vow("hEelLoooO") == 6
    assert vowels.vow("Hello") == 2