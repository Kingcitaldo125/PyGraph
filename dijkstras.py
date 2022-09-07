from collections import defaultdict

class Node:
    def __init__(self, name, dist = 9999):
        self.name = name
        self.distance = dist

    def __str__(self):
        return self.get_name()

    def __eq__(self, other):
        return self.name == other.get_name() and self.distance == other.get_distance()

    def update_distance(self, val):
        self.distance = val

    def get_name(self):
        return str(self.name)

    def get_distance(self):
        return self.distance

class Graph:
    def __init__(self):
        self.nodes = []
        self.node_names = set()
        self.edges = set()

    def add_node(self, node: Node):
        if not node:
            print('Must pass in a valid node to add it.')
            return

        if self.exists(node.get_name()):
            return

        self.nodes.append(node)
        self.node_names.add(node.get_name())

    def add_edge(self, node_a: Node, node_b: Node, weight):
        if not node_a or not node_b:
            print('Must pass in valid nodes to add edges.')
            return

        if not self.exists(node_a.get_name()):
            print(f'Node {node_a} doesn\'t exist in the graph.')
            return

        if not self.exists(node_b.get_name()):
            print(f'Node {node_b} doesn\'t exist in the graph.')
            return

        self.edges.add((node_a.get_name(), node_b.get_name(), weight))

    def get_node_by_name(self, node_name):
        for node in self.nodes:
            if node.get_name() == node_name:
                return node

        return None

    def exists(self, node_name):
        return node_name in self.node_names

    def get_neighbors(self, node_name):
        if not self.exists(node_name):
            return []

        mlist = []
        mset = set()
        for itm in self.edges:
            node_1, node_2, weight = itm[0], itm[1], itm[2]

            if node_1 == node_name and node_2 not in mset:
                mlist.append([self.get_node_by_name(node_2), weight])
                mset.add(node_2)

        return mlist

def update_distance(current_node, neighbor, weight):
    nname = neighbor.get_name()
    msum = current_node.get_distance() + weight
    neigh_dist = neighbor.get_distance()

    if msum < neigh_dist:
        neighbor.update_distance(msum)
        new_dist = neighbor.get_distance()
        print(f"Updated neighbor '{nname}' distance from '{neigh_dist}' to '{new_dist}'")

def dijkstras(graph, start_node, end_node):
    mqueue = []
    visited = set([start_node.get_name()])
    path = []

    mqueue.insert(0, start_node)

    while len(mqueue) > 0:
        itm = mqueue.pop()
        itm_name = itm.get_name()

        print(f'Visited {itm}')

        path.append(itm_name)

        smallest_weight = 9999
        neighbors = graph.get_neighbors(itm_name)

        if itm_name == end_node.get_name():
            return path

        for neigh, weight in neighbors:
            nname = neigh.get_name()

            if nname not in visited:
                smallest_weight = min(weight, smallest_weight)

            update_distance(itm, neigh, weight)

        for neigh, weight in neighbors:
            nname = neigh.get_name()

            if nname not in visited and weight <= smallest_weight:
                visited.add(nname)
                mqueue.insert(0, neigh)

    return []

mgraph = Graph()

start_node = 'a'
nodes = set(['b','c','d','e','f'])

mgraph.add_node(Node(start_node, dist=0))
for n in nodes:
    mgraph.add_node(Node(n))

mgraph.add_edge(mgraph.get_node_by_name('a'), mgraph.get_node_by_name('b'), 3)
mgraph.add_edge(mgraph.get_node_by_name('a'), mgraph.get_node_by_name('c'), 8)
mgraph.add_edge(mgraph.get_node_by_name('b'), mgraph.get_node_by_name('d'), 1)
mgraph.add_edge(mgraph.get_node_by_name('b'), mgraph.get_node_by_name('e'), 2)
mgraph.add_edge(mgraph.get_node_by_name('c'), mgraph.get_node_by_name('d'), 1)
mgraph.add_edge(mgraph.get_node_by_name('c'), mgraph.get_node_by_name('f'), 2)
mgraph.add_edge(mgraph.get_node_by_name('d'), mgraph.get_node_by_name('b'), 1)
mgraph.add_edge(mgraph.get_node_by_name('d'), mgraph.get_node_by_name('c'), 1)
mgraph.add_edge(mgraph.get_node_by_name('d'), mgraph.get_node_by_name('f'), 5)

path = dijkstras(mgraph, mgraph.get_node_by_name('a'), mgraph.get_node_by_name('f'))

print('path:', path) # a -> b -> d -> c -> f
