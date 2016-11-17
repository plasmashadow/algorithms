from collections import Iterable, Hashable, Container


class Traversor(Iterable):

    def __init__(self, root):
        self.root = root

    def __iter__(self):
        raise NotImplemented


class InorderTraversor(Traversor):

    def __init__(self, *args, **kwargs):
        super(InorderTraversor, self).__init__(*args, **kwargs)

    def __iter__(self):
        for l in iter(self.root.left):
            yield l
        yield self.root
        for r in iter(self.root.right):
            yield r


class PreOrderTraversor(Traversor):

    def __init__(self, *args, **kwargs):
        super(PreOrderTraversor, self).__init__(*args, **kwargs)

    def __iter__(self):
        yield self.root
        for l in iter(self.root.left):
            yield l
        for r in iter(self.root.right):
            yield r


class PostOrderTraversor(Traversor):

    def __init__(self, *args, **kwargs):
        super(PostOrderTraversor, self).__init__(*args, **kwargs)

    def __iter__(self):
        for l in iter(self.root.left):
            yield l
        for r in iter(self.root.right):
            yield r
        yield self.root


class BinaryNode(Hashable):
    def __init__(self, val, _id=None):
        self._value = val
        self._id = _id
        self.left = None
        self.right = None
        self._size_of_subtree = 0

    @property
    def is_leaf(self):
        return not self.left and not self.right

    def __eq__(self, other):
        return self._value == other._value

    def __hash__(self):
        return hash(self)


class BinaryTree(Container):

    def __init__(self, root):
        self._root = root
        self._nodes = {}
        self._rootNode = BinaryNode(root)

    def _find(self, key, root):
        if root is None:
            return None
        node_key = BinaryNode(key)
        if node_key < node:
            return self._find(key, node.left)
        elif node_key > node:
            return self._find(key, node.right)
        else:
            return BinaryNode(node_key._value, node_key._id)

    def find(self, key):
        return self._find(key, self._rootNode)

    def _put(self, key, _id, node):
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
        return node

    def put(self, key, _id):
        return self._put(self, key, _id, self._rootNode)

    def _min(self, node):
        if node.left:
            return self._min(node.left)
        return node

    @property
    def min(self):
        return self._min(self._rootNode)

    def _max(self, node):
        if node.right:
            return self._max(node.right)
        return node

    @property
    def max(self):
        return self._max(self._rootNode)

    def _size(self, node):
        if node is None:
            return 0
        return node._size_of_subtree

    def __len__(self):
        return self._size(self._rootNode)

    def __contains__(self, key):
        return self.find(key) is not None

    def __iter__(self):
    	return InorderTraversor(self._rootNode)

    def preorder(self):
    	return PreOrderTraversor(self._rootNode)

    def postorder(self):
    	return PostOrderTraversor(self._rootNode)
