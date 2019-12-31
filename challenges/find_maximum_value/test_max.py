from max import Node, BinarySearchTree, BinaryTree, find_maximum_value

def test_empty_tree():
    tree = BinarySearchTree()
    actual = find_maximum_value(tree)
    expected = None
    assert actual == expected

def test_one():
    tree = BinarySearchTree()
    tree.add(77)
    actual = find_maximum_value(tree)
    expected = 77
    assert actual == expected

def test_three():
    tree = BinarySearchTree()
    tree.add(77)
    tree.add(66)
    tree.add(88)
    actual = find_maximum_value(tree)
    expected = 88
    assert actual == expected

def test_more():
    tree = BinarySearchTree()
    tree.add(50)
    tree.add(45)
    tree.add(55)
    tree.add(40)
    tree.add(60)
    tree.add(35)
    tree.add(65)
    actual = find_maximum_value(tree)
    expected = 65
    assert actual == expected