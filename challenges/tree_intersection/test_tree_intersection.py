import pytest
from tree_intersection import *
from tree import *


def test_one():
    expected = 5, 6, 7
    actual = tree_intersection((1,2,3,4,5,6,7),(12,23,34,45,5,6,7))
    assert expected == actual