"""
Graph Data Structure

A graph data structure consists of a finite (and possibly mutable)
set of vertices or nodes or points,
together with a set of unordered pairs of these vertices
for an undirected graph or a set of
ordered pairs for a directed graph. These pairs are known as edges, arcs,
or lines for an undirected graph and as arrows, directed edges, directed arcs,
or directed lines for a directed graph.
The vertices may be part of the graph structure,
or may be external entities represented by integer indices or references.
"""
from collections import defaultdict


class Vertex(object):
    """
      Node in a graph is called a Vertex
      Contains data and pointer to nearest
      neighbors.
    """
    def __init__(self, data):
        self.data = data
        self.neighbors = {}

    def add_neighbor(self, neighbor, weight=0):
        """Add a neighbor
           Time Complexity O(1)
        """
        self.neighbors[neighbor] = weight

    @property
    def adj(self):
        """returns a nearest nodes"""
        return self.neighbors.keys()

    def get_weight(self, node):
        """get the edge weight of adjecent node"""
        return self.neighbors.get(node, 0)

    def remove_neighbor(self, neighbor):
        """remove a neighbor"""
        return self.neighbors.pop(neighbor)

    def __eq__(self, other):
        return self.data == other.data

    def __hash__(self):
        return hash(self.data)


class Graph(object):
    """
    G = f(V, E)
    where G is the graph.
    V - Set of vertices
    E - Edges between vertices

    Representation:
       1) Adjecency List.
       2) Adjecency Matrix.

    Current implementation depends on Adjecency List. Which holds the List
    of nearest neighbors to each Vertex.
    """
    def neighbors(self, x):
        raise NotImplemented

    def add_vertex(self, x):
        raise NotImplemented

    def add_edge(self, x, y, weight=0):
        raise NotImplemented

    def remove_edge(self, x, y):
        raise NotImplemented

    def find_path(self, x, y, path=[]):
        raise NotImplemented

    @property
    def size(self):
        return self._numvertex


class UndirectedGraph(Graph):
    """ UNDIRECTED GRAPH
    An undirected graph is a graph in which edges have no orientation.
    The edge (x, y) is identical to the edge (y, x),
    i.e., they are not ordered pairs,
    but sets {x, y} (or 2-multisets) of vertices.
    The maximum number of edges in an undirected graph without a
    loop is n(n − 1)/2.
    """

    def __init__(self):
        self.vertexlist = {}
        self._numvertex = 0

    def add_vertex(self, x):
        """Adds a new vertex to the existing graph
           Time Complexity: O(1)
        """
        if x in self.vertexlist:
            return
        vrx = Vertex(x)
        self.vertexlist[x] = vrx
        self._numvertex += 1
        return vrx

    def add_edge(self, x, y, weight=0):
        """Adds a new edge between adjecent node
           Time Complexity: O(1)
        """
        if x not in self.vertexlist:
            raise Exception("Not a Vertex, %d" % x)
        if y not in self.vertexlist:
            raise Exception("Not a Vertex, %d" % y)

        self.vertexlist[x].add_neighbor(self.vertexlist[y], weight)
        self.vertexlist[y].add_neighbor(self.vertexlist[x], weight)

    @property
    def vertices(self):
        return self.vertexlist.keys()

    def neighbors(self, x):
        vertex = self.vertexlist.get(x)
        if vertex:
            return vertex.adj
        return None

    def remove_edge(self, x, y):
        """Removes the edges between adjecent nodes
           Time Complexity: O(1)
        """
        if x not in self.vertexlist:
            raise Exception("Not a Vertex, %d" % x)
        if y not in self.vertexlist:
            raise Exception("Not a Vertex, %d" % y)
        self.vertexlist[x].remove_neighbor(self.vertexlist[y])
        self.vertexlist[y].remove_neighbor(self.vertexlist[x])

    def __contains__(self, x):
        return x in self.vertexlist

    def find_path(self, _from, _to, path=[]):
        """Doing a breath first search to get the path between
           nodes (May not be shortest)
           Time Complexity: O(V) + O(E) = O(V+E)
        """
        path = path + [_from]
        if _from == _to:
            return path
        if _from not in self:
            return []
        for node in self.vertexlist:
            if node not in path:
                new_path = self.find_path(node, _to, path)
                if new_path:
                    return new_path
        return []


class DirectedGraph(Graph):
    """
    a directed graph (or digraph) is a graph
    (that is a set of vertices connected by edges),
    where the edges have a direction associated with them.
    """

    def __init__(self):
        self.vertexlist = defaultdict(list)
        self._numvertex = 0

    def add_vertex(self, data):
        """Add a new vertex into the existing graph
        Time Complexity: O(1)
        """
        if data in self.vertexlist:
            return
        vrx = Vertex(data)
        self.vertexlist[data] = vrx
        self._numvertex += 1
        return vrx

    def add_edge(self, x, y, weight=0):
        """Adds a new directed edge between x and y
           Time Complexity: O(1)
        """
        if x not in self.vertexlist:
            raise Exception("Not a Vertex, %d" % x)
        if y not in self.vertexlist:
            raise Exception("Not a Vertex, %d" % y)
        self.vertexlist[x].add_neighbor(self.vertexlist[y], weight)

    @property
    def vertices(self):
        return self.vertexlist.keys()

    def neighbors(self, x):
        vertex = self.vertexlist.get(x)
        if vertex:
            return vertex.adj
        return None

    def remove_edge(self, x, y):
        """Removes the edges between adjecent nodes
           Time Complexity: O(1)
        """
        if x not in self.vertexlist:
            raise Exception("Not a Vertex, %d" % x)
        if y not in self.vertexlist:
            raise Exception("Not a Vertex, %d" % y)
        self.vertexlist[x].remove_neighbor(self.vertexlist[y])

    def __contains__(self, x):
        return x in self.vertexlist

    def find_path(self, _from, _to, path=[]):
        """Doing a breath first search to get the path between
           nodes (May not be shortest)
           Time Complexity: O(V) + O(E) = O(V+E)
        """
        path = path + [_from]
        if _from == _to:
            return path
        if _from not in self:
            return []
        for node in self.vertexlist:
            if node not in path and Vertex(node) in self.neighbors(_from):
                new_path = self.find_path(node, _to, path)
                if new_path:
                    return new_path
        return []
