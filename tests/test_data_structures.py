from random import shuffle
import unittest

from algorithms.data_structures import (
    tree,
    binary_tree,
    disjoint_set,
    queue,
    linked_list,
    stack,
    graph,
    lcp_array
)


class TestTreeInterface(unittest.TestCase):

    """Test Tree Interface"""

    def test_tree_interface(self):
        self.tree = tree.Tree(1)
        self.tree.add(2, parent=1)
        self.tree.add(4, parent=1)
        self.tree.add(3, parent=2)
        self.tree.add(5, parent=4)
        self.assertTrue(1 in self.tree)
        self.assertTrue(2 in self.tree)
        self.assertEqual(2, self.tree.get_degree(1))
        self.assertEqual(1, self.tree.get_degree(4))
        self.assertEqual(0, self.tree.get_degree(3))
        self.assertEqual([1, 2, 4, 3, 5], list(iter(self.tree)))
        self.assertEqual([1, 2, 3, 4, 5], list(self.tree.dfs()))


class TestBST(unittest.TestCase):

    """Test For Binary Search Tree"""

    def setUp(self):
        self.bst = binary_tree.BinaryTree(5, "a")
        self.bst.put(4, "b")
        self.bst.put(6, "c")
        self.bst.put(2, "d")
        self.bst.put(7, "e")
        self.bst.put(8, "f")

    def test_add_leaf_nodes(self):
        self.assertTrue(7 in self.bst)
        self.assertTrue(2 in self.bst)

    def test_min_object_in_tree(self):
        self.assertEqual(self.bst.min._value, 2)
        self.assertEqual(self.bst.min._id, "d")
        self.bst.put(1, "z")
        self.assertEqual(self.bst.min._value, 1)

    def test_max_object_in_tree(self):
        self.assertEqual(self.bst.max._value, 8)
        self.assertEqual(self.bst.max._id, "f")

    def test_tree_delete(self):
        self.bst.delete(1)
        self.assertFalse(1 in self.bst)
        self.bst.delete(7)
        self.assertEqual(self.bst.max._id, "f")

    def test_tree_inorder_traversal(self):
        lst = list(iter(self.bst))
        self.assertEqual(lst, [2, 4, 5, 6, 7, 8])

    def test_tree_preorder_traversal(self):
        lst = list(self.bst.preorder())
        self.assertEqual(lst, [5, 4, 2, 6, 7, 8])

    def test_tree_postorder_traversal(self):
        lst = list(self.bst.postorder())
        self.assertEqual(lst, [2, 4, 8, 7, 6, 5])

    def test_size_of_tree(self):
        self.assertEqual(len(self.bst), 6)
        self.bst.delete(8)
        self.bst.delete(7)
        self.assertEqual(len(self.bst), 4)

    def test_rank_of_tree(self):
        self.assertEqual(self.bst.rank(5), 2)


class TestGraphInterface(unittest.TestCase):

    def test_undirected_graph_interface(self):
        self.gp = graph.UndirectedGraph()
        self.gp.add_vertex(1)
        self.gp.add_vertex(2)
        self.gp.add_vertex(3)
        self.assertTrue(1 in self.gp)
        self.assertTrue(2 in self.gp)
        self.gp.add_edge(1, 2, weight=1)
        self.assertEqual(len(self.gp.neighbors(1)), 1)
        self.gp.add_edge(1, 3, weight=1)
        self.assertEqual(len(self.gp.neighbors(1)), 2)
        self.assertTrue(graph.Vertex(2) in self.gp.neighbors(1))
        self.assertEqual([1, 2, 3], self.gp.find_path(1, 3))

    def test_directed_graph_interface(self):
        self.gp = graph.DirectedGraph()
        self.gp.add_vertex(1)
        self.gp.add_vertex(2)
        self.gp.add_vertex(3)
        self.gp.add_vertex(5)
        self.assertTrue(1 in self.gp)
        self.assertTrue(2 in self.gp)
        self.gp.add_edge(1, 2, weight=1)
        self.assertEqual(len(self.gp.neighbors(1)), 1)
        self.gp.add_edge(1, 3, weight=1)
        self.assertEqual(len(self.gp.neighbors(1)), 2)
        self.assertTrue(graph.Vertex(2) in self.gp.neighbors(1))
        self.gp.add_edge(3, 5, weight=4)
        self.assertEqual([1, 3, 5], self.gp.find_path(1, 5))


class TestQueue(unittest.TestCase):

    """
    Test Queue Implementation
    """

    def test_queue(self):
        self.que = queue.Queue()
        self.que.add(1)
        self.que.add(2)
        self.que.add(8)
        self.que.add(5)
        self.que.add(6)
        self.assertTrue(5 in self.que)
        self.assertEqual(self.que.remove(), 1)
        self.assertEqual(self.que.size(), 4)
        self.assertEqual(self.que.remove(), 2)
        self.assertEqual(self.que.remove(), 8)
        self.assertEqual(self.que.remove(), 5)
        self.assertEqual(self.que.remove(), 6)
        self.assertEqual(self.que.is_empty(), True)


class TestSinglyLinkedList(unittest.TestCase):

    """
    Test Singly Linked List Implementation
    """

    def test_singly_linked_list(self):
        self.sl = linked_list.SinglyLinkedList()
        self.sl.append(10)
        self.sl.append(5)
        self.sl.append(30)
        self.sl.remove(30)
        self.sl.append_front(1)

        self.assertFalse(30 in self.sl)
        self.assertTrue(5 in self.sl)
        self.assertTrue(10 in self.sl)
        self.assertEqual(3, self.sl.size)
        self.assertEqual(1, self.sl.head.data)

    def test_doubly_linked_list(self):
        self.sl = linked_list.DoublyLinkedList()
        self.sl.append(10)
        self.sl.append(5)
        self.sl.append(30)
        self.sl.remove(30)
        self.sl.append_front(1)

        self.assertFalse(30 in self.sl)
        self.assertTrue(5 in self.sl)
        self.assertTrue(10 in self.sl)
        self.assertEqual(3, self.sl.size)
        self.assertEqual(1, self.sl.head.data)


class TestStack(unittest.TestCase):

    """
    Test Stack Implementation
    """

    def test_stack(self):
        self.sta = stack.Stack()
        self.sta.add(5)
        self.sta.add(8)
        self.sta.add(10)
        self.sta.add(2)

        self.assertEqual(self.sta.remove(), 2)
        self.assertEqual(self.sta.is_empty(), False)
        self.assertEqual(self.sta.size(), 3)


class TestUnionFind(unittest.TestCase):

    """
    Test Union Find Implementation
    """

    def test_union_find(self):
        self.uf = disjoint_set.DistjointSet(0, 1, 2, 3, 4)
        self.uf.union(1, 0)
        self.uf.union(3, 4)

        self.assertEqual(self.uf.find(1), 0)
        self.assertEqual(self.uf.find(3), 4)
        self.assertEqual(self.uf.is_connected(0, 1), True)
        self.assertEqual(self.uf.is_connected(3, 4), True)


class TestUnionFindByRank(unittest.TestCase):

    """
    Test Union Find Implementation
    """

    def test_union_find_by_rank(self):
        self.uf = disjoint_set.DisjointSetWithUnionRank(0, 1, 2, 3, 4, 5, 6)
        self.uf.union(1, 0)
        self.uf.union(3, 4)
        self.uf.union(2, 4)
        self.uf.union(5, 2)
        self.uf.union(6, 5)

        self.assertEqual(self.uf.find(1), 1)
        self.assertEqual(self.uf.find(3), 3)
        # test tree is created by rank
        self.uf.union(5, 0)
        self.assertEqual(self.uf.find(2), 3)
        self.assertEqual(self.uf.find(5), 3)
        self.assertEqual(self.uf.find(6), 3)
        self.assertEqual(self.uf.find(0), 3)

        self.assertEqual(self.uf.is_connected(0, 1), True)
        self.assertEqual(self.uf.is_connected(3, 4), True)
        self.assertEqual(self.uf.is_connected(5, 3), True)


class TestUnionFindWithPathCompression(unittest.TestCase):

    """
    Test Union Find Implementation
    """

    def test_union_find_with_path_compression(self):
        self.uf = (
            disjoint_set
            .DisjointSetWithPathCompression(0, 1, 2, 3, 4, 5)
        )

        self.uf.union(0, 1)
        self.uf.union(2, 3)
        self.uf.union(1, 3)
        self.uf.union(4, 5)
        self.assertEqual(self.uf.find(1), 3)
        self.assertEqual(self.uf.find(3), 3)
        self.assertEqual(self.uf.parent(3), 3)
        self.assertEqual(self.uf.parent(5), 5)
        self.assertEqual(self.uf.is_connected(3, 5), False)
        self.assertEqual(self.uf.is_connected(4, 5), True)
        self.assertEqual(self.uf.is_connected(2, 3), True)
        # test tree is created by path compression
        self.uf.union(5, 3)
        self.assertEqual(self.uf.parent(3), 3)

        self.assertEqual(self.uf.is_connected(3, 5), True)


class TestLCPSuffixArrays(unittest.TestCase):

    def setUp(self):
        super(TestLCPSuffixArrays, self).setUp()
        self.case_1 = "aaaaaa"
        self.s_array_1 = [5, 4, 3, 2, 1, 0]
        self.rank_1 = [5, 4, 3, 2, 1, 0]
        self.lcp_1 = [1, 2, 3, 4, 5, 0]

        self.case_2 = "abcabcdd"
        self.s_array_2 = [0, 2, 4, 1, 3, 5, 7, 6]
        self.rank_2 = [0, 3, 1, 4, 2, 5, 7, 6]
        self.lcp_2 = [3, 0, 2, 0, 1, 0, 1, 0]

        self.case_3 = "kmckirrrmppp"
        self.s_array_3 = [3, 4, 0, 2, 1, 11, 10, 9, 5, 8, 7, 6]
        self.rank_3 = [2, 4, 3, 0, 1, 8, 11, 10, 9, 7, 6, 5]
        self.lcp_3 = [0, 0, 1, 0, 1, 0, 1, 2, 0, 1, 2, 0]

    def test_lcp_array(self):
        lcp = lcp_array.lcp_array(self.case_1, self.s_array_1, self.rank_1)
        self.assertEqual(lcp, self.lcp_1)

        lcp = lcp_array.lcp_array(self.case_2, self.s_array_2, self.rank_2)
        self.assertEqual(lcp, self.lcp_2)

        lcp = lcp_array.lcp_array(self.case_3, self.s_array_3, self.rank_3)
        self.assertEqual(lcp, self.lcp_3)

    def test_suffix_array(self):
        s_array, rank = lcp_array.suffix_array(self.case_1)
        self.assertEqual(s_array, self.s_array_1)
        self.assertEqual(rank, self.rank_1)

        s_array, rank = lcp_array.suffix_array(self.case_2)
        self.assertEqual(s_array, self.s_array_2)
        self.assertEqual(rank, self.rank_2)

        s_array, rank = lcp_array.suffix_array(self.case_3)
        self.assertEqual(s_array, self.s_array_3)
        self.assertEqual(rank, self.rank_3)
