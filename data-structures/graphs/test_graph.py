import pytest

from graph import Graph, Vertex

def test_add_node():

    graph = Graph()

    expected = 'bacon-bits'

    actual = graph.add_node('bacon-bits').value

    assert actual == expected

def test_size_empty():

    graph = Graph()

    expected = 0

    actual = graph.size()

    assert actual == expected


def test_size():

    graph = Graph()

    graph.add_node('bacon-bits')

    expected = 1

    actual = graph.size()

    assert actual == expected


def test_add_edge_interloper_start():

    graph = Graph()

    start = Vertex('start')

    end = graph.add_node('end')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)




def test_add_edge_interloper_end():

    graph = Graph()

    end = Vertex('end')

    start = graph.add_node('start')

    with pytest.raises(KeyError):
        graph.add_edge(start, end)


def test_add_edge_groovy():

    graph = Graph()

    end = graph.add_node('end')

    start = graph.add_node('start')

    graph.add_edge(start, end)

def test_add_edge_effect():

    graph = Graph()

    end = graph.add_node('turkey')

    start = graph.add_node('candy')

    graph.add_edge(start, end)

    expected = (end, 0)

    actual = graph.alike[start][0]

    assert actual == expected

def test_add_edge_effect_with_weight():

    graph = Graph()

    end = graph.add_node('turkey')

    start = graph.add_node('candy')

    graph.add_edge(start, end, 44)

    expected = (end, 44)

    actual = graph.alike[start][0]

    assert actual == expected


def test_get_nodes():

    graph = Graph()

    turkey = graph.add_node('turkey')

    candy = graph.add_node('candy')

    solo = Vertex('solo')

    expected = 2

    actual = len(graph.get_nodes())

    assert actual == expected


def test_get_neighbors():

    graph = Graph()

    turkey = graph.add_node('turkey')

    candy = graph.add_node('candy')

    graph.add_edge(candy, turkey, 44)

    neighbors = graph.get_neighbors(candy)


    assert len(neighbors) == 1

    assert neighbors[0][0].value == 'turkey'

    assert isinstance(neighbors[0][0], Vertex)

    assert neighbors[0][1] == 44