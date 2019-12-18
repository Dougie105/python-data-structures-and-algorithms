import pytest
from fifo_animal_shelter import (
    Animal_Shelter,
    EmptyListError,
    NonShelterAnimal,
    Pet,
    Cat,
    Dog,
    Fish,
)


def test_shelter():
    assert Animal_Shelter()


def test_cat():
    assert Dog("Peeve")


def test_dog():
    assert Cat("Karma")


@pytest.fixture()
def shelter():
    return Animal_Shelter()


def test_add_remove_one_dog(shelter):
    shelter.enqueue(Dog("alvin"))
    shelter.enqueue(Cat("barb"))
    assert shelter.dequeue("dog").name == "alvin"


def test_add_remove_one_cat(shelter):
    shelter.enqueue(Dog("chester"))
    shelter.enqueue(Cat("doggo"))
    assert shelter.dequeue("cat").name == "doggo"


def test_add_remove_multi_cat(shelter):
    shelter.enqueue(Cat("eric"))
    shelter.enqueue(Cat("fred"))
    assert shelter.dequeue("cat").name == "eric"
    assert shelter.dequeue("cat").name == "fred"


def test_add_non_valid_pet(shelter):
    with pytest.raises(NonShelterAnimal):
        shelter.enqueue(Fish("Gillbert"))


def test_remove_from_empty(shelter):
    with pytest.raises(EmptyListError):
        shelter.dequeue("cat")


def test_remove_non_valid_pet(shelter):
    assert shelter.dequeue("fish") == None

