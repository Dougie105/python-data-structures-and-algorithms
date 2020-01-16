from quick_sort import quick_sort
import pytest


def test_scrambled_order():
    lst = quick_sort([32,675,87,985,6534,43,54,65,8,8,542,2,6,87,1,5,9])
    assert lst == [1, 2, 5, 6, 8, 8, 9, 32, 43, 54, 65, 87, 87, 542, 675, 985, 6534]

def test_already_sorted():
    lst = quick_sort([1, 2, 5, 6, 8, 8, 9, 32, 43, 54, 65, 87, 87, 542, 675, 985, 6534])
    assert lst == [1, 2, 5, 6, 8, 8, 9, 32, 43, 54, 65, 87, 87, 542, 675, 985, 6534]

def test_mixed_quick():
    lst = quick_sort([-32,-675,87,985,6534,-43,54,-65,8,-8,542,2,6,-87,1,5,9,])
    assert lst == [-675, -87, -65, -43, -32, -8, 1, 2, 5, 6, 8, 9, 54, 87, 542, 985, 6534]
