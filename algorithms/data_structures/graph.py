"""
Graph Data Structure

A graph data structure consists of a finite (and possibly mutable) set of vertices or nodes or points, 
together with a set of unordered pairs of these vertices for an undirected graph or a set of 
ordered pairs for a directed graph. These pairs are known as edges, arcs,
or lines for an undirected graph and as arrows, directed edges, directed arcs,
or directed lines for a directed graph. The vertices may be part of the graph structure, 
or may be external entities represented by integer indices or references.
"""


class Vertex(object):
	def __init__(self, data):
		self.data = data
		self.neighbors = {}

	def add_neighbor(self, neighbor, weight=0):
		self.neighbors[neighbor] = weight

	@property
	def adj(self):
		return self.neighbors.keys()

	def get_weight(self, node):
		return self.neighbors.get(node, 0)

	def remove_neighbor(self, neighbor):
		return self.neighbors.pop(neighbor)

	def __eq__(self, other):
		return self.data == other.data


class Graph(object):


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

	def __init__(self):
		self.vertexlist = {}
		self._numvertex = 0

	def add_vertex(self, x):
		if x in self.vertexlist:
			return
		vrx = Vertex(x)
		self.vertexlist[x] = vrx
		self._numvertex += 1
		return vrx

	def add_edge(self, x, y, weight=0):

		if x not in self.vertexlist:
			raise Exception("Not a Vertex, %d" %x)
		if y not in self.vertexlist:
			raise Exception("Not a Vertex, %d" %y)

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
		if x not in self.vertexlist:
			raise Exception("Not a Vertex, %d" %x)
		if y not in self.vertexlist:
			raise Exception("Not a Vertex, %d" %y)
		self.vertexlist[x].remove_neighbor(self.vertexlist[y])
		self.vertexlist[y].remove_neighbor(self.vertexlist[x])

	def __contains__(self, x):
		return x in self.vertexlist

	def find_path(self, _from, _to, path=[]):
		"""Doing a breath first search to get the path between 
		   nodes (May not be shortest)
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







