import pytest
from Code import route_planner

def test_route():
    assert route_planner.peak([2,3,2,3,4,1,5]) == [1,2,3,4,5]

    