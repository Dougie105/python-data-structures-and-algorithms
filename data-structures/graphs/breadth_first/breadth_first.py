import inspect, re, collections
from graph import Graph

class NewGraph(Graph):
    def breadth_first(self, vertex):

        visited = set()
        dq = collections.deque()
        dq.appendleft(vertex)

        while dq:
            current = dq.pop()
            visited.add(current)
            lst = self.get_neighbors(current)
            if lst:
                for edge in lst:
                    if edge[0] not in visited:
                        dq.appendleft(edge[0])

        return visited


class Vertex:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return self.value

if __name__ == "__main__":
    graph = NewGraph()