import pytest
from Code import sort_string

def test_s_str():
    assert sort_string.s_str("without,hello,bag,world") == "bag,hello,without,world"