import pytest
from Code import generate_dictionary

def dic_gen_test():
    assert generate_dictionary.dic_gen(5) == {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}