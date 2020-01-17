from hashtable import Node, HashTable
import pytest

hash = HashTable

def test_add_to_table():
    '''Adding a key/value to your hashtable results in the value being in the data structure'''
    hash = HashTable()
    hash.add('dog', 'bark')
    hash.add('cat', 'bark')
    hash.add('bird', 'bark')
    hash.add('mouse', 'bark')
    hash.add('person', 'bark')
    expected = 5
    actual = hash.size
    assert expected == actual

def test_get():
    '''Retrieving based on a key returns the value stored'''
    hash = HashTable()
    hash.add('dog', 'bark')
    hash.add('Freddie', 'Nightmare')
    actual = hash.get('Freddie')
    expected = 'Nightmare'
    assert expected == actual

def test_get_null():
    '''Successfully returns null for a key that does not exist in the hashtable'''
    hash = HashTable()
    hash.add('dog', 'bark')
    hash.add('Freddie', 'Nightmare')
    hash.add('Jason', 'Lake')
    actual = hash.contains('Frankie')
    expected = False
    assert expected == actual

def test_get_collision():
    '''Successfully handle a collision within the hashtable'''
    hash = HashTable()
    hash.add('dog', 'bark')
    hash.add('god', 'karb')
    actual = hash.contains('dog')
    actual = hash.contains('god')
    expected = True
    assert expected == actual

def test_get_form_collision():
    '''Successfully retrieve a value from a bucket within the hashtable that has a collision'''
    hash = HashTable()
    hash.add('dog', 'bark')
    hash.add('god', 'karb')
    actual = hash.get('dog')
    expected = 'bark'
    assert expected == actual

def test_in_range():
    '''Successfully hash a key to an in-range value'''
    hash = HashTable()
    actual = hash.hash('dog')
    expected = 30
    assert expected == actual