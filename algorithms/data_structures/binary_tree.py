from collections import Hashable, Container


def inorder(node):
    if node is not None:
        for l in inorder(node.left):
            yield l
        yield node._value
        for l in inorder(node.right):
            yield l


def preorder(node):
    if node is not None:
        yield node._value
        for l in preorder(node.left):
            yield l
        for l in preorder(node.right):
            yield l


def postorder(node):
    if node is not None:
        for l in postorder(node.left):
            yield l
        for l in postorder(node.right):
            yield l
        yield node._value


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

    def __lt__(self, other):
        return self._value < other._value

    def __gt__(self, other):
        return self._value > other._value

    def __hash__(self):
        return hash(self)

    def __iter__(self):
        return inorder(self)


class BinaryTree(Container):

    def __init__(self, root, _id):
        self._root = root
        self._nodes = {}
        self._rootNode = BinaryNode(root, _id)

    def _find(self, key, node):
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
        return self._put(key, _id, self._rootNode)

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
        return self._rootNode._size_of_subtree

    def __contains__(self, key):
        return self.find(key) is not None

    def __iter__(self):
        return iter(self._rootNode)

    def preorder(self):
        return iter(preorder(self._rootNode))

    def postorder(self):
        return iter(postorder(self._rootNode))

    def _delete(self, key, node):
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
        self._rootNode = self._delete(key, self._rootNode)

    def pprint(self):
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
