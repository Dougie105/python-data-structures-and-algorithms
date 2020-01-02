import pytest
from max import BinaryTree

def test_add_one_to_tree():
    new_tree = BinaryTree()
    new_tree.add(2)
    assert new_tree.root.value == 2

def test_add_three_to_tree():
    new_tree = BinaryTree()
    new_tree.add(2)
    assert new_tree.root.value == 2
    new_tree.add(7)
    assert new_tree.root.left.value == 7
    new_tree.add(5)
    assert new_tree.root.right.value == 5

def test_maximum_value():
    new_tree = BinaryTree()
    expected = 97
    new_tree.add(22)
    new_tree.add(73)
    new_tree.add(54)
    new_tree.add(23)
    new_tree.add(26)
    new_tree.add(97)
    new_tree.add(51)
    new_tree.add(11)
    new_tree.add(4)
    assert new_tree.find_maximum_value() == expected

def test_negative_max():
    new_tree = BinaryTree()
    expected = -34
    new_tree.add(-42)
    new_tree.add(-53)
    new_tree.add(-57)
    new_tree.add(-65)
    new_tree.add(-72)
    new_tree.add(-86)
    new_tree.add(-89)
    new_tree.add(-95)
    new_tree.add(-911)
    new_tree.add(-34)
    assert new_tree.find_maximum_value() == expected