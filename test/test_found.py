import pytest

from Graph.Graph import Graph

@pytest.fixture
def nodes_wide():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

@pytest.fixture
def nodes_deep():
    return ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

@pytest.fixture
def wide_graph(nodes_wide):
    graph = Graph()

    for n in nodes_wide:
        graph.add_node(n)

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("B", "E")
    graph.add_edge("C", "F")
    graph.add_edge("C", "G")
    graph.add_edge("D", "H")
    graph.add_edge("D", "I")
    graph.add_edge("E", "J")
    graph.add_edge("E", "K")
    graph.add_edge("F", "L")
    graph.add_edge("F", "M")
    graph.add_edge("G", "N")
    graph.add_edge("G", "O")

    return graph

@pytest.fixture
def deep_graph(nodes_deep):
    graph = Graph()

    for n in nodes_deep:
        graph.add_node(n)

    graph.add_edge("A", "B")

    graph.add_edge("B", "D")
    graph.add_edge("D", "E")
    graph.add_edge("E", "F")
    graph.add_edge("F", "G")
    graph.add_edge("G", "H")

    graph.add_edge("A", "C")

    graph.add_edge("C", "I")
    graph.add_edge("I", "J")
    graph.add_edge("J", "K")
    graph.add_edge("K", "L")
    graph.add_edge("L", "M")

    return graph

def test_graph_wide_bfs(nodes_wide, wide_graph):
    nodes = nodes_wide

    ln = len(nodes) - 1

    results = [False for i in range(ln)]

    graph = wide_graph

    for i,j in enumerate(nodes[1:]):
        results[i] = graph.hasPathBFS('A', j)

    assert results == [True for i in range(ln)]

def test_graph_deep_bfs(nodes_deep, deep_graph):
    nodes = nodes_deep

    ln = len(nodes) - 1

    results = [False for i in range(ln)]

    graph = deep_graph

    for i,j in enumerate(nodes[1:]):
        results[i] = graph.hasPathBFS('A', j)

    assert results == [True for i in range(ln)]

def test_graph_wide_dfs(nodes_wide, wide_graph):
    nodes = nodes_wide

    ln = len(nodes) - 1

    results = [False for i in range(ln)]

    graph = wide_graph

    for i,j in enumerate(nodes[1:]):
        results[i] = graph.hasPathDFS('A', j)

    assert results == [True for i in range(ln)]

def test_graph_deep_dfs(nodes_deep, deep_graph):
    nodes = nodes_deep

    ln = len(nodes) - 1

    results = [False for i in range(ln)]

    graph = deep_graph

    for i,j in enumerate(nodes[1:]):
        results[i] = graph.hasPathDFS('A', j)

    assert results == [True for i in range(ln)]
