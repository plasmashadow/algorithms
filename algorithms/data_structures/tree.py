"""
TREE DATA STRUCTURE
===================
 A tree is a widely used abstract data type (ADT) data structure implementing
 this ADT—that simulates a hierarchical tree structure, with a root value
 and subtrees of children with a parent node, represented as
 a set of linked nodes.
"""

from collections import Container, Hashable


class TreeNode(Container, Hashable):
    """Abstract node for a tree"""
    def __init__(self, data):
        self.data = data
        self.children = list()

    def add_child(self, identifier):
        self.children.append(identifier)

    def remove_child(self, node):
        if node not in self.children:
            return
        self.children.remove(node)

    @property
    def degree(self):
        return len(self.children)

    def __hash__(self):
        return hash(self)

    def __contains__(self, other):
        return self == other or other in self.children

    def __eq__(self, other):
        return self.data == other.data

    def __le__(self, other):
        return self.data <= other.data

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data


class Tree(object):
    """Generic tree implementation
        T = f(e, v)
        where e- element in node.
              v- list of children.
    """
    def __init__(self, root=None):
        if not root:
            raise Exception("Root required")
        self.root = root
        self.root_node = TreeNode(root)
        self.__nodes = {}
        self.__nodes[self.root] = self.root_node

    def add(self, identifier, parent=None):
        node = TreeNode(identifier)
        self[identifier] = node
        if parent is not None:
            self[parent].add_child(identifier)
        else:
            self[root].add_child(identifier)

    def __getitem__(self, item):
        return self.__nodes[item]

    def __setitem__(self, key, item):
        self.__nodes[key] = item

    def get_degree(self, identifier):
        return self[identifier].degree

    @property
    def nodes(self):
        return self.__nodes.keys()

    def __iter__(self):
        yield self.root
        queue = self[self.root].children
        while queue:  # doing a bfs
            yield queue[0]
            path = self[queue[0]].children
            queue = queue[1:] + path

    def __contains__(self, id):
        return id in self.__nodes

    def dfs(self):
        yield self.root
        queue = self[self.root].children
        while queue:  # doing a dfs
            yield queue[0]
            path = self[queue[0]].children
            queue = path + queue[1:]