"""
    Union Find:
    -----------
    A disjoint-set data structure, also called union-find data structure
    implements two functions:

    union(A, B) - merge A's set with B's set

    find(A) - finds what set A belongs to


    Naive approach:

    Find follows parent nodes until it reaches the root.
    Union combines two trees into one by attaching the root of one to the
    root of the other

    Time Complexity  :  O(N) (a highly unbalanced tree might be created,
    nothing better a linked-list)

    Psuedo Code: http://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class DistjointSet(object):

    def __init__(self, *args):
        if len(args) < 0:
            raise ValueError("N cannot be a negative integer")
        self._parent = []
        self._N = len(args)
        for i in args:
            self._parent.append(i)

    def make_set(self, x):
        if type(x) != int:
            raise TypeError("x must be integer")
        if x != self._N:
            raise ValueError(
                "a new element must have index {0}".format(self._N)
            )
        self._parent.append(x)
        self._N = self._N + 1

    def union(self, x, y):
        self._validate_ele(x)
        self._validate_ele(y)
        x_root = self.find(x)
        y_root = self.find(y)
        self._parent[x_root] = y_root

    def find(self, x):
        self._validate_ele(x)
        if self._parent[x] == x:
            return x
        else:
            return self.find(self._parent[x])

    def is_connected(self, x, y):
        self._validate_ele(x)
        self._validate_ele(y)
        return self.find(x) == self.find(y)

    def _validate_ele(self, x):
        if type(x) != int:
            raise TypeError("{0} is not an integer".format(x))
        if x < 0 or x >= self._N:
            raise ValueError("{0} is not in [0,{1})".format(x, self._N))

    def parent(self, x):
        return self._parent[x]


class DisjointSetWithPathCompression(DistjointSet):

    def __init__(self, *args):
        super(DisjointSetWithPathCompression, self).__init__(*args)

    def _find(self, x):
        if self._parent[x] != x:
            self._parent[x] = self._find(self._parent[x])
        return self._parent[x]

    def find(self, x):
        self._validate_ele(x)
        if self._parent[x] == x:
            return x
        else:
            return self._find(self._parent[x])

    def _validate_ele(self, x):
        if type(x) != int:
            raise TypeError("{0} is not an integer".format(x))
        if x < 0 or x >= self._N:
            raise ValueError("{0} is not in [0,{1})".format(x, self._N))


class DisjointSetWithUnionRank(DistjointSet):

    def __init__(self, *args):
        super(DisjointSetWithUnionRank, self).__init__(*args)
        self._rank = []
        self._N = len(args)
        for i in args:
            self._rank.append(0)

    def union(self, x, y):
        self._validate_ele(x)
        self._validate_ele(y)
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        # x and y are not already in same set. Merge them
        if self._rank[x_root] < self._rank[y_root]:
            self._parent[x_root] = y_root
        elif self._rank[x_root] > self._rank[y_root]:
            self._parent[y_root] = x_root
        else:
            self._parent[y_root] = x_root
            self._rank[x_root] = self._rank[x_root] + 1

    def make_set(self, x):
        if type(x) != int:
            raise TypeError("x must be integer")
        if x != self._N:
            raise ValueError(
                "a new element must have index {0}".format(self._N))
        self._parent.append(x)
        self._rank.append(0)
        self._N = self._N + 1

    def _validate_ele(self, x):
        if type(x) != int:
            raise TypeError("{0} is not an integer".format(x))
        if x < 0 or x >= self._N:
            raise ValueError("{0} is not in [0,{1})".format(x, self._N))
