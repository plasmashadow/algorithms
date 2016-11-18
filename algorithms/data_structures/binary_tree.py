
"""
BST
===
In computer science, binary search trees (BST),
sometimes called ordered or sorted binary trees,
are a particular type of containers: data structures that store in memory.
They allow fast lookup, addition and removal of items,
and can be used to implement either dynamic sets of items,
or lookup tables that allow finding an item by its key.
"""

from collections import Hashable, Container


def inorder(node):
	"""Travel left-> root -> right"""
    if node is not None:
        for l in inorder(node.left):
            yield l
        yield node._value
        for l in inorder(node.right):
            yield l


def preorder(node):
	"""Travel root-> left -> right"""
    if node is not None:
        yield node._value
        for l in preorder(node.left):
            yield l
        for l in preorder(node.right):
            yield l


def postorder(node):
	"""Travel left-> right -> root"""
    if node is not None:
        for l in postorder(node.left):
            yield l
        for l in postorder(node.right):
            yield l
        yield node._value


class BinaryNode(Hashable):
	"""
	A node in a binary tree consists of a value,
	key - which uniquly identifies the node
	and left and right subtrees. When other node
	gets added to the current node. It will increase
	the size of the current node's subpath.
	"""

    def __init__(self, val, _id=None):
        self._value = val
        self._id = _id
        self.left = None
        self.right = None
        self._size_of_subtree = 1

    @property
    def is_leaf(self):
        return not self.left and not self.right

    def __eq__(self, other):
        if isinstance(other, int):
            return self._value == other
        return self._value == other._value

    def __lt__(self, other):
        if isinstance(other, int):
            return self._value < other
        return self._value < other._value

    def __gt__(self, other):
        if isinstance(other, int):
            return self._value > other
        return self._value > other._value

    def __hash__(self):
        return hash(self)

    def __iter__(self):
        return inorder(self)


class BinaryTree(Container):
	"""
	Binary tree provides efficent mechanism of storing and 
	searching items. Since the tree is always sorted.
	We know exactly where the retrival will take place.
	"""

    def __init__(self, root, _id):
        self._root = root
        self._nodes = {}
        self._rootNode = BinaryNode(root, _id)

    def _find(self, key, node):
    	"""Find a node with a given key
    	Time Complexity
    	 O(log N) - Balanced Tree 
    	 O(N) - Worst case
    	"""
        if node is None:
            return None
        node_key = BinaryNode(key)
        if node_key < node:
            return self._find(key, node.left)
        elif node_key > node:
            return self._find(key, node.right)
        else:
            return BinaryNode(node_key._value, node_key._id)

    def find(self, key):
    	"""Find a node with a given key
    	Time Complexity
    	 O(log N) - Balanced Tree 
    	 O(N) - Worst case
    	"""
        return self._find(key, self._rootNode)

    def _put(self, key, _id, node):
    	"""Puts a node with a given key
    	Time Complexity
    	 O(log N) - Balanced Tree 
    	 O(N) - Worst case
    	"""
        if node is None:
            return BinaryNode(key, _id)
        node_key = BinaryNode(key, _id)
        if node_key < node:
            node.left = self._put(key, _id, node.left)
        elif node_key > node:
            node.right = self._put(key, _id, node.right)
        else:
            node._value = key
        node._size_of_subtree = \
            self._size(node.left) + self._size(node.right) + 1
        print(node._value, node._size_of_subtree)
        return node

    def put(self, key, _id):
    	"""Puts a node with a given key
    	Time Complexity
    	 O(log N) - Balanced Tree 
    	 O(N) - Worst case
    	"""
        return self._put(key, _id, self._rootNode)

    def _min(self, node):
    	"""Gets a minimum node"""
        if node.left:
            return self._min(node.left)
        return node

    @property
    def min(self):
    	"""Gets the minimum node in the tree"""
        return self._min(self._rootNode)

    def _max(self, node):
    	"""gets the maximum node"""
        if node.right:
            return self._max(node.right)
        return node

    @property
    def max(self):
    	"""gets the bigger node in the tree"""
        return self._max(self._rootNode)

    def _size(self, node):
    	"""gets the number of element in the tree"""
        if node is None:
            return 0
        return node._size_of_subtree

    def __len__(self):
        return self._size(self._rootNode)

    def __contains__(self, key):
        return self.find(key) is not None

    def __iter__(self):
    	"""Traverses the elements inorder"""
        return iter(self._rootNode)

    def preorder(self):
    	"""Traverses the elements in preorder"""
        return iter(preorder(self._rootNode))

    def postorder(self):
    	"""Traverses thee element in postorder"""
        return iter(postorder(self._rootNode))

    def _delete(self, key, node):
    	"""Deletes a node with the given key
    	Time Complexity:
    	O(N) = Worst Case
    	O(log N) = Balanced Binary Tree
    	"""
        if node is None:
            return node
        node_key = BinaryNode(key)
        if node_key < node:
            node.left = self._delete(node_key._value, node.left)
        elif node_key > node:
            node.right = self._delete(node_key._value, node.right)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                temp = self._min(node.right)
                node._value = temp._value
                node._id = node._value
                node.right = self._delete(temp._value, node.right)
                node.left = temp.left
        node._size_of_subtree = self._size(node.left) \
            + self._size(node.right) + 1
        return node

    def delete(self, key):
    	"""Deletes a node with the given key
    	Time Complexity:
    	O(N) = Worst Case
    	O(log N) = Balanced Binary Tree
    	"""
        self._rootNode = self._delete(key, self._rootNode)

    def pprint(self):
    	"""Pretty Prints the given binary Tree"""
        current_level = [self._rootNode]
        while current_level:
            next_level = []
            for n in current_level:
                print(n._value)
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            print()
            current_level = next_level
