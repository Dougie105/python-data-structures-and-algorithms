from breadth_first import Vertex, NewGraph
import pytest

def test_no_edges():
    graph = NewGraph()

    # add all nodes
    badger = graph.add_node('badger')
    armidillo = graph.add_node('armidillo')
    hedgehog = graph.add_node('hedgehog')
    spider = graph.add_node('spider')
    ardvark = graph.add_node('ardvark')
    octopus = graph.add_node('octopus')

    assert graph.breadth_first(badger) == {badger}

def test_breadth_first():
    graph = NewGraph()

    # add all nodes
    badger = graph.add_node('badger')
    armidillo = graph.add_node('armidillo')
    hedgehog = graph.add_node('hedgehog')
    spider = graph.add_node('spider')
    ardvark = graph.add_node('ardvark')
    octopus = graph.add_node('octopus')

    # add all edges
    graph.add_edge(badger, armidillo, 1)

    graph.add_edge(armidillo, badger, 2)
    graph.add_edge(armidillo, hedgehog, 3)
    graph.add_edge(armidillo, octopus, 4)

    graph.add_edge(hedgehog, armidillo, 5)
    graph.add_edge(hedgehog, octopus, 6)
    graph.add_edge(hedgehog, spider, 7)

    graph.add_edge(octopus, armidillo, 8)
    graph.add_edge(octopus, hedgehog, 9)
    graph.add_edge(octopus, spider, 10)
    graph.add_edge(octopus, ardvark, 20)

    graph.add_edge(spider, hedgehog, 30)
    graph.add_edge(spider, octopus, 40)
    graph.add_edge(spider, ardvark, 50)

    graph.add_edge(ardvark, octopus, 60)
    graph.add_edge(ardvark, spider, 70)

    assert graph.breadth_first(badger) == {badger, spider, ardvark, hedgehog, octopus, armidillo}


def test_directional_edges():
    graph = NewGraph()

    # add all nodes
    badger = graph.add_node('badger')
    armidillo = graph.add_node('armidillo')
    hedgehog = graph.add_node('hedgehog')
    spider = graph.add_node('spider')
    ardvark = graph.add_node('ardvark')
    octopus = graph.add_node('octopus')

    # add some edges
    graph.add_edge(badger, armidillo, 1)

    graph.add_edge(armidillo, octopus, 4)

    graph.add_edge(octopus, ardvark, 20)


    assert graph.breadth_first(badger) == {badger, armidillo, octopus, ardvark}