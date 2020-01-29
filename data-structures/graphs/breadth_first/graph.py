class Graph:
    def __init__(self):
        self.alike = {}

    def add_node(self, value):
        vertex = Vertex(value)

        self.alike[vertex] = []

        return vertex

    def size(self):
        return len(self.alike)

    def add_edge(self, start, end, weight=0):

        if start not in self.alike:
            raise KeyError("Start not in Graph")

        if end not in self.alike:
            raise KeyError("End not in Graph")

        adjacencies = self.alike[start]

        adjacencies.append((end, weight))

    def get_nodes(self):
        return self.alike.keys()

    def get_neighbors(self, vertex):
        return self.alike[vertex]


class Vertex:
    def __init__(self, value):
        self.value = value
