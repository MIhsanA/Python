import pytest
from Code import password_validity

def test_pass_validity():
    assert password_validity.pass_validity(["ABd1234@1","a F1#","2w3E*","2We3345"]) ==["ABd1234@1"]