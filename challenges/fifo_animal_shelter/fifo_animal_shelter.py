class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class Pet:
    def __init__(self, name):
        self.name = name


class Cat(Pet):
    pass


class Dog(Pet):
    pass


class Fish(Pet):
    pass


class EmptyListError(AssertionError):
    pass


class NonShelterAnimal(ValueError):
    pass


class Queue:
    def __init__(self, front=None):
        self.front = front
        self.end = end_next = self.front
        while end_next:
            if isinstance(end_next, Node):
                self.end = end_next
                end_next = end_next.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.end = new_node
        else:
            self.end.next = self.end = new_node

    def dequeue(self):
        if self.is_empty():
            raise EmptyListError("The List is Empty")
        removed = self.front
        self.front = self.front.next
        return removed.value

    def peek(self):
        if not self.is_empty():
            return self.front.value
        raise EmptyListError("The List is Empty")

    def is_empty(self):
        if self.front:
            return False
        return True


class Animal_Shelter:
    def __init__(self):
        """
    Creating 2 queues for cats and dogs.
    """
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, pet):
        if isinstance(pet, Dog):
            self.dog_queue.enqueue(pet)
        elif isinstance(pet, Cat):
            self.cat_queue.enqueue(pet)
        else:
            raise NonShelterAnimal

    def dequeue(self, pet=None):
        if pet.lower() == "dog":
            return self.dog_queue.dequeue()
        elif pet.lower() == "cat":
            return self.cat_queue.dequeue()
        return None

