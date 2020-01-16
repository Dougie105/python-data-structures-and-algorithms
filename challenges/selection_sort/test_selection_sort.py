import pytest
from selection_sort import selection_sort


def test_reverse_order():
    new_arr = selection_sort([8,7,6,5,4,3,2,1])
    assert new_arr == [1,2,3,4,5,6,7,8]

def test_already_sorted():
    new_arr = selection_sort([1,2,3,4,5,6,7,8])
    assert new_arr == [1,2,3,4,5,6,7,8]

def test_negative_sorted():
    new_arr = selection_sort([-1,-2,-3,-4,-5,-6,-7,-8])
    assert new_arr == [-8,-7,-6,-5,-4,-3,-2,-1]

def test_mixed_sorted():
    new_arr = selection_sort([-1,2,-3,-46,65,-6,17,-8])
    assert new_arr == [-46,-8,-6,-3,-1,2,17,65]