import pytest
from Code import combine_srt

def test_comb_str():
    assert combine_srt.comb_str("String","Fridge") == "SFtrriidngge"