from array_binary_search import binary_search

def test_one():
    expected = 2
    actual = binary_search([4, 8, 15, 16, 23, 44], 15)
    assert expected == actual

def test_two():
    expected = -1
    actual = binary_search([4, 8, 15, 16, 23, 44], 30)
    assert expected == actual

def test_three():
    expected = -1
    actual = binary_search([4, 8, 15, 16, 23, 44], 2)
    assert expected == actual