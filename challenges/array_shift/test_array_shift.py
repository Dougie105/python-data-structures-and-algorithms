from array_shift import insert_shift_array

def test_one():
    expected = [1, 2, 3, 'pickle', 4, 5, 6]
    actual = insert_shift_array([1, 2, 3, 4, 5, 6], 'pickle')
    assert expected == actual


def test_two():
    expected = [1, 2, 3, 'pickle', 4, 5]
    actual = insert_shift_array([1, 2, 3, 4, 5], 'pickle')
    assert expected == actual